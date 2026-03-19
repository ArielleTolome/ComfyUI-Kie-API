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

### Available Templates

**Images (`prompts/images/`)**
- `grid_visual_director.txt`: System prompt for designing shot plans and variations for real-camera-style AI imagery.
- `image_grid_storyboard.txt`: System prompt for generating structured JSON output describing a grid of image prompts for a single campaign concept.
- `character_extraction_prompt.txt`: System prompt for describing a character extracted via Sora 2 Characters Pro node in a single concise sentence.

**Videos (`prompts/videos/`)**
- `wan_i2v_grid_story_director.txt`: System prompt for WAN 2.1/2.2 I2V generation.
- `final_expense_ad_creative.txt`: System prompt for generating Final Expense insurance ad video scripts.
- `video_prompt_expander.txt`: System prompt that takes a short concept description and expands it into a detailed, model-optimized video generation prompt.

Notes:
- This README is ignored by the node.
- If `{user_prompt}` is missing, the user prompt is appended at the end.
