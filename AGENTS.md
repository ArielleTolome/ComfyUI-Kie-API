**Project Overview**
- This is a ComfyUI custom node pack that connects to the Kie.ai API
- All nodes are defined in nodes.py and registered in __init__.py
- API key is loaded from config/kie_key.txt at runtime
- If KIE_API_KEY environment variable is present, it takes priority over the file

**Node Architecture**
- Every node follows the same pattern: INPUT_TYPES classmethod defines inputs, a main method calls the Kie.ai API, polls async until complete using the existing polling helper, and returns the output
- Async polling timeout is set to 2000 seconds
- All image inputs arrive as ComfyUI IMAGE tensors (BCHW format) and must be converted to base64 before sending to the API
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