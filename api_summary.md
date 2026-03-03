# API Parameter Summary

Based on an inspection of the live Kie.ai model pages:

**(a) What is current and matches:**
- **Sora 2:** The current node implementations in `nodes.py` (`sora-2-image-to-video`, `sora-2-text-to-video`, `sora-2-image-to-video-stable`, `sora-2-text-to-video-stable`, `sora-2-characters-pro`, `sora-watermark-remover`) perfectly match the parameters exposed on the live API page (e.g., `prompt`, `image_urls`, `aspect_ratio` (portrait, landscape), `n_frames` (10, 15), `upload_method` (s3, oss), `remove_watermark`, `origin_task_id`, `character_user_name`, `character_prompt`, `safety_instruction`, `video_url`).

**(b) What is new or changed:**
- **Seedream:** The live API page exposes a model under the path `bytedance/seedream` (or `seedream`). This endpoint requires the parameters: `prompt`, `image_size` (`square`, `square_hd`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`), `guidance_scale`, `seed`, and `enable_safety_checker`. In contrast, the current codebase implements `seedream/4.5-text-to-image` and `seedream/4.5-edit` which accept `aspect_ratio` (`1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `2:3`, `3:2`, `21:9`) and `quality` (`basic`, `high`). This indicates a new model tier or significant parameter changes for Seedream.
- **Kling, Seedance, Flux, Suno, Gemini:** The live API pages for these models returned HTTP 404 (Not Found) errors. Therefore, it is impossible to verify if the live API has introduced new parameters, renamed fields, or deprecated options for these models.

**(c) What needs a new node or update:**
- **Seedream:** A new node (e.g., `KIE_Seedream_API`) needs to be created, or the existing ones updated, to support the new `bytedance/seedream` model and its parameters (`image_size`, `guidance_scale`, `seed`, `enable_safety_checker`).
- **Kling, Seedance, Flux, Suno, Gemini:** Cannot be determined due to the 404 errors. No changes are recommended until the live API pages become accessible and can be reviewed.
