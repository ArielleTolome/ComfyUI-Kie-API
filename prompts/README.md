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

#### Image Prompts (`prompts/images/`)
- **Grid Visual Director (Real Camera - Influencer Style)** (`grid_visual_director.txt`): Designs shot plans, pose variations, camera logic, and editorial rhythm for real-camera-style AI imagery.
- **Image Grid Storyboard JSON** (`image_grid_storyboard.txt`): Generates structured JSON output describing a grid of image prompts based on a campaign concept, parseable by the Prompt Grid JSON Parser node.
- **Character Extraction Prompt** (`character_extraction_prompt.txt`): Describes a character extracted via the Sora 2 Characters Pro node as a single concise sentence of stable traits.

#### Video Prompts (`prompts/videos/`)
- **WAN 2.1/2.2 I2V Grid Story Director (v5)** (`wan_i2v_grid_story_director.txt`): Converts a composite grid image and a creative directive into a sequence of independent WAN-compatible I2V prompts.
- **Final Expense Ad Creative** (`final_expense_ad_creative.txt`): Generates Final Expense insurance ad video scripts, focusing on emotional resonance, compliance, and family protection.
- **Video Prompt Expander** (`video_prompt_expander.txt`): Expands short concepts into detailed, model-optimized video generation prompts for models like Kling and Sora 2.

Notes:
- This README is ignored by the node.
- If `{user_prompt}` is missing, the user prompt is appended at the end.
