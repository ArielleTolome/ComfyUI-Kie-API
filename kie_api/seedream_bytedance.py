"""Seedream 3.0 (bytedance/seedream) text-to-image helper.

Implements the ``bytedance/seedream`` model exposed on the Kie.ai API.
This is a separate model tier from the existing ``seedream/4.5`` nodes with
a different parameter set: ``image_size``, ``guidance_scale``, ``seed``, and
``enable_safety_checker`` replace the legacy ``aspect_ratio`` / ``quality`` inputs.

API reference: https://kie.ai/seedream (Seedream 3.0 endpoint)
"""

import time

import torch

from .auth import _load_api_key
from .credits import _log_remaining_credits
from .images import _download_image, _image_bytes_to_tensor
from .jobs import _create_task, _poll_task_until_complete
from .log import _log
from .results import _extract_result_urls
from .validation import _validate_prompt


MODEL_NAME = "bytedance/seedream"

IMAGE_SIZE_OPTIONS = [
    "square",
    "square_hd",
    "portrait_4_3",
    "portrait_16_9",
    "landscape_4_3",
    "landscape_16_9",
]

PROMPT_MAX_LENGTH = 3000
GUIDANCE_SCALE_MIN = 1.0
GUIDANCE_SCALE_MAX = 10.0


def _validate_image_size(image_size: str) -> None:
    if image_size not in IMAGE_SIZE_OPTIONS:
        raise RuntimeError(
            f"Invalid image_size '{image_size}'. "
            f"Valid options: {', '.join(IMAGE_SIZE_OPTIONS)}"
        )


def _validate_guidance_scale(guidance_scale: float) -> None:
    if not (GUIDANCE_SCALE_MIN <= guidance_scale <= GUIDANCE_SCALE_MAX):
        raise RuntimeError(
            f"guidance_scale must be between {GUIDANCE_SCALE_MIN} and "
            f"{GUIDANCE_SCALE_MAX} (got {guidance_scale})."
        )


def run_seedream_bytedance_text_to_image(
    prompt: str,
    image_size: str,
    guidance_scale: float,
    seed: int,
    enable_safety_checker: bool,
    poll_interval_s: float,
    timeout_s: int,
    log: bool,
) -> torch.Tensor:
    """Generate an image using the Seedream 3.0 (bytedance/seedream) model.

    Args:
        prompt: Text prompt describing the desired image.
        image_size: Output dimensions/aspect ratio enum (e.g. ``square_hd``).
        guidance_scale: Prompt adherence strength (1.0–10.0).
        seed: Random seed for reproducible outputs; -1 for random.
        enable_safety_checker: Whether to run the safety filter on the output.
        poll_interval_s: Seconds between status polls.
        timeout_s: Maximum seconds to wait for completion.
        log: Enable verbose console logging.

    Returns:
        ComfyUI IMAGE tensor (1, H, W, 3) float32 in [0, 1].

    Raises:
        RuntimeError: For validation errors or non-retryable API failures.
        TransientKieError: For retryable API/task failures.
    """
    _validate_prompt(prompt, max_length=PROMPT_MAX_LENGTH)
    _validate_image_size(image_size)
    _validate_guidance_scale(guidance_scale)

    api_key = _load_api_key()

    input_payload: dict = {
        "prompt": prompt,
        "image_size": image_size,
        "guidance_scale": guidance_scale,
        "enable_safety_checker": enable_safety_checker,
    }
    # Only include seed when explicitly set; -1 means "let the API randomise"
    if seed >= 0:
        input_payload["seed"] = seed

    payload = {
        "model": MODEL_NAME,
        "input": input_payload,
    }

    _log(log, f"Creating Seedream 3.0 (bytedance/seedream) task [image_size={image_size}, "
         f"guidance_scale={guidance_scale}, seed={seed if seed >= 0 else 'random'}, "
         f"safety={enable_safety_checker}]...")
    start_time = time.time()
    task_id, create_response_text = _create_task(api_key, payload)
    _log(log, f"createTask response (elapsed={time.time() - start_time:.1f}s): {create_response_text}")
    _log(log, f"Task {task_id} created. Polling for completion...")

    record_data = _poll_task_until_complete(
        api_key,
        task_id,
        poll_interval_s,
        timeout_s,
        log,
        start_time,
    )

    result_urls = _extract_result_urls(record_data)
    _log(log, f"Result URLs: {result_urls}")
    _log(log, f"Downloading result image from {result_urls[0]}...")

    image_bytes = _download_image(result_urls[0])
    image_tensor = _image_bytes_to_tensor(image_bytes)
    _log(log, "Image downloaded and decoded.")

    _log_remaining_credits(log, record_data, api_key, _log)
    return image_tensor
