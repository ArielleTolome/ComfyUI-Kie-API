"""Sora 2 image-to-video helper."""

import time
from typing import Any

import torch

from .auth import _load_api_key
from .credits import _log_remaining_credits
from .jobs import _create_task, _poll_task_until_complete
from .log import _log
from .results import _extract_result_urls
from .upload import _image_tensor_to_png_bytes, _truncate_url, _upload_image
from .validation import _validate_image_tensor_batch, _validate_prompt
from .video import _download_video, _video_bytes_to_comfy_video


MODEL_OPTIONS = ["sora-2-image-to-video", "sora-2-image-to-video-stable"]
PROMPT_MAX_LENGTH = 10000
ASPECT_RATIO_OPTIONS = ["landscape", "portrait"]
DURATION_OPTIONS = ["10", "15"]


def run_sora2_i2v_video(
    prompt: str,
    images: torch.Tensor,
    model: str,
    aspect_ratio: str,
    n_frames: str,
    remove_watermark: bool,
    poll_interval_s: float,
    timeout_s: int,
    log: bool,
) -> dict:
    _validate_prompt(prompt, max_length=PROMPT_MAX_LENGTH)
    if model not in MODEL_OPTIONS:
        raise RuntimeError("Invalid model. Use the pinned enum options.")
    if aspect_ratio not in ASPECT_RATIO_OPTIONS:
        raise RuntimeError("Invalid aspect_ratio. Use the pinned enum options.")
    if n_frames not in DURATION_OPTIONS:
        raise RuntimeError("Invalid n_frames. Use the pinned enum options.")
    images = _validate_image_tensor_batch(images)

    api_key = _load_api_key()

    if images.shape[0] > 1:
        _log(log, f"More than 1 image provided ({images.shape[0]}); only the first will be used.")

    _log(log, "Uploading source image for Sora 2 I2V...")
    png_bytes = _image_tensor_to_png_bytes(images[0])
    image_url = _upload_image(api_key, png_bytes)
    _log(log, f"Image upload success: {_truncate_url(image_url)}")

    payload = {
        "model": model,
        "input": {
            "prompt": prompt,
            "image_urls": [image_url],
            "aspect_ratio": aspect_ratio,
            "n_frames": n_frames,
            "remove_watermark": remove_watermark,
        },
    }

    _log(log, f"Creating Sora 2 I2V task (model={model})...")
    start_time = time.time()
    task_id, create_response_text = _create_task(api_key, payload)
    _log(log, f"createTask response (elapsed={time.time() - start_time:.1f}s): {create_response_text}")
    _log(log, f"Task created with ID {task_id}. Polling for completion...")

    record_data = _poll_task_until_complete(
        api_key,
        task_id,
        poll_interval_s,
        timeout_s,
        log,
        start_time,
    )

    result_urls = _extract_result_urls(record_data)
    video_url = result_urls[0]
    _log(log, f"Final video URL: {video_url}")

    video_bytes = _download_video(video_url)
    video_output = _video_bytes_to_comfy_video(video_bytes)

    _log_remaining_credits(log, record_data, api_key, _log)
    return video_output
