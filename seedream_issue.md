# Title: Update or Add Node for `bytedance/seedream` (Seedream 3.0 API)

## Description
The live Kie.ai API page (https://kie.ai/seedream) exposes a new model path `bytedance/seedream` (referred to as Seedream 3.0 API in the UI) with a completely different set of parameters compared to the existing `seedream/4.5` implementations in our codebase.

### What is currently implemented:
We currently have `KIE_Seedream45_TextToImage` and `KIE_Seedream45_Edit` supporting the model `seedream/4.5`.
- **Inputs:** `prompt`, `aspect_ratio` (`1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `2:3`, `3:2`, `21:9`), and `quality` (`basic`, `high`).

### What is required (live API):
The new `bytedance/seedream` model requires the following inputs:
- `prompt` (string, required): The text prompt used to generate the image.
- `image_size` (enum): Specifies the aspect ratio and resolution. Valid options: `square`, `square_hd`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`.
- `guidance_scale` (number): Controls how closely the output image aligns with the input prompt (e.g., slider from 1 to 10).
- `seed` (number): Random seed to control the stochasticity of image generation.
- `enable_safety_checker` (boolean): Whether to enable the safety checker (typically true by default).

## Action Items
1. **Create a new node** (e.g., `KIE_Seedream_Bytedance_TextToImage`) in `nodes.py` to support the new `bytedance/seedream` model path.
2. Update the API helper module (or create a new one, e.g., `seedream_bytedance.py` inside `kie_api/`) to handle the `image_size`, `guidance_scale`, `seed`, and `enable_safety_checker` payload structure.
3. Keep the existing Seedream 4.5 nodes intact unless they are confirmed deprecated by Kie.ai.
4. Update documentation in `web/docs/` to reflect the new Seedream 3.0 API node.
