**Project Overview**
- This is a ComfyUI custom node pack that connects to the Kie.ai API
- All nodes are defined in nodes.py and registered in __init__.py
- API key is loaded from `config/kie_key.txt` at runtime (see `kie_api/auth.py`)
- Environment variable override is not currently implemented; to add it, update `_load_api_key()` in `kie_api/auth.py` to check `os.environ.get('KIE_API_KEY')` first

**Node Architecture**
- Every node follows the same pattern: INPUT_TYPES classmethod defines inputs, a main method calls the Kie.ai API, polls async until complete using the existing polling helper, and returns the output
- Async polling timeout is set to 2000 seconds
- All image inputs arrive as ComfyUI IMAGE tensors in BHWC format `[B, H, W, 3]`; individual frames are passed as `[H, W, 3]` tensors and converted to PNG bytes via `_image_tensor_to_png_bytes()` in `kie_api/upload.py`, then uploaded directly (not base64-encoded)
- VIDEO outputs are returned as file paths or URLs depending on the node

**File Map**
- nodes.py — all node implementations
- __init__.py — NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS
- config/kie_key.txt — API key storage (gitignored)
- kie_api/ — API client helpers and polling logic
- web/docs/ — one markdown doc per node, named KIE_<NodeName>.md
- example_workflows/ — ComfyUI workflow JSON files
- prompts/ — system prompt templates for the System Prompt Selector node
- pyproject.toml — version and metadata

**Adding a New Node Checklist**
1. Implement the node class in nodes.py following the existing pattern
2. Register in NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS in __init__.py
3. Create web/docs/KIE_<NodeName>.md documentation
4. Bump patch version in pyproject.toml
5. Add changelog entry in README.md

**Testing**
- Use the KIE_GetRemainingCredits node as a lightweight API health check
- The KIE_API_KEY environment variable must be set for any live API tests
- Do not make generation calls (image/video/audio) during automated testing as they consume credits

**Known Experimental Nodes**
- Kling 3.0 — marked experimental, not production-ready as of the last sync