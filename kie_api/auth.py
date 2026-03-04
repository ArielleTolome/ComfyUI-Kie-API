import os
from pathlib import Path


KIE_KEY_PATH = Path(__file__).resolve().parent.parent / "config" / "kie_key.txt"


def _load_api_key() -> str:
    """Load the KIE API key.

    Resolution order:
    1. ``KIE_API_KEY`` environment variable (takes priority when set and non-empty).
    2. ``config/kie_key.txt`` file relative to the repo root.

    Raises:
        RuntimeError: If the key cannot be found or is empty.
    """
    env_key = os.environ.get("KIE_API_KEY", "").strip()
    if env_key:
        return env_key

    try:
        api_key = KIE_KEY_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "KIE API key not found. Set the KIE_API_KEY environment variable "
            "or create config/kie_key.txt with your API key."
        ) from exc
    if not api_key:
        raise RuntimeError(
            "KIE API key is empty. Set the KIE_API_KEY environment variable "
            "or add your key to config/kie_key.txt."
        )
    return api_key
