# System Prompt Templates

Put your system prompt templates in subfolders as `.txt` files:
- Image prompts go in `prompts/images/`
- Video prompts go in `prompts/videos/`

Each template file must include:
- A `name:` line for the dropdown label
- A `system prompt below` line marking the start of the template body
- Optional `{user_prompt}` placeholder for insertion

Create a new prompt by placing a `.txt` file in the appropriate folder, adding the `name:` line at the top, then `system prompt below`, then your full system prompt text.

Example:
```
name: Character Consistency v1
system prompt below
You are a helpful assistant. Always preserve the character's identity.
When the user says: {user_prompt}
Return concise instructions for image generation.
```

Notes:
- This README is ignored by the node.
- If `{user_prompt}` is missing, the user prompt is appended at the end.

## Available Templates

### Image Prompts (`prompts/images/`)
- `grid_visual_director.txt` (Grid Visual Director (Real Camera - Influencer Style)): Designs shot plans, pose variation, camera logic, and editorial rhythm for real-camera-style AI imagery.
- `image_grid_storyboard.txt` (Image Grid Storyboard (JSON)): Generates structured JSON output describing a 2x2 or 3x3 grid of image prompts for a single campaign concept, parseable by the Prompt Grid JSON Parser node.

### Video Prompts (`prompts/videos/`)
- `wan_i2v_grid_story_director.txt` (WAN 2.1/2.2 I2V Grid Story Director (v5)): Converts a composite grid image and user directive into a sequence of independent WAN-compatible I2V prompts in a cohesive storyboard.
- `final_expense_ad_creative.txt` (Final Expense Ad Creative): Generates emotionally resonant, compliance-aware video ad scripts targeting seniors aged 50-85 for Final Expense insurance marketing.
- `video_prompt_expander.txt` (Video Prompt Expander (Kling/Sora2)): Expands a short concept description into a detailed, model-optimized prompt for video generation (Kling/Sora 2), including camera, lighting, and mood.
- `character_extraction_prompt.txt` (Character Extraction (Sora 2)): Condenses a character description into a single concise sentence of stable traits, suitable for direct use as a character_prompt input.
