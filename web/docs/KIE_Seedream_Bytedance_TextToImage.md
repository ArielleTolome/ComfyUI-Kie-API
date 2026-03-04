# KIE Seedream 3.0 (bytedance) Text-To-Image

Generate images using the **Seedream 3.0** model (`bytedance/seedream`) via the Kie.ai API.

This is a newer model tier than Seedream 4.5 with a different parameter set. Use `image_size` (aspect-ratio enum) instead of `aspect_ratio`, and control output detail with `guidance_scale` and `seed`.

---

## Inputs

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | STRING | ✅ | — | Text prompt describing the desired image (max 3000 chars) |
| `image_size` | COMBO | | `square_hd` | Output dimensions / aspect ratio (see options below) |
| `guidance_scale` | FLOAT | | `7.5` | How closely the output follows the prompt (1.0 = loose, 10.0 = strict) |
| `seed` | INT | | `-1` | Random seed for reproducibility; `-1` = random each run |
| `enable_safety_checker` | BOOLEAN | | `True` | Run safety filter on the generated image |
| `poll_interval_s` | FLOAT | | `10.0` | Seconds between status polls (1–60) |
| `timeout_s` | INT | | `2000` | Max seconds to wait for completion (min effective: 2000s) |
| `log` | BOOLEAN | | `True` | Enable verbose console logging |

### `image_size` options

| Value | Description |
|---|---|
| `square` | Square output (standard resolution) |
| `square_hd` | Square output (high resolution) — **default** |
| `portrait_4_3` | Portrait 4:3 |
| `portrait_16_9` | Portrait 16:9 |
| `landscape_4_3` | Landscape 4:3 |
| `landscape_16_9` | Landscape 16:9 |

---

## Outputs

| Name | Type | Description |
|---|---|---|
| `image` | IMAGE | ComfyUI image tensor (BHWC float32, values in [0, 1]) |

---

## Notes

- **Seedream 3.0 vs 4.5:** The `bytedance/seedream` model uses `image_size` + `guidance_scale` + `seed` rather than the `aspect_ratio` + `quality` parameters of `seedream/4.5`. Keep both node types available — 4.5 is not deprecated.
- **Seed reproducibility:** Set `seed` to any non-negative integer to get deterministic results from the same prompt and settings. Use `-1` for random variation.
- **Safety checker:** Disabling `enable_safety_checker` may allow generation of content that would otherwise be filtered. Leave enabled unless you have a specific reason.
- **Timeout:** The internal polling engine enforces a minimum of 2000 seconds regardless of the `timeout_s` setting.

---

## API Reference

- Model path: `bytedance/seedream`
- Endpoint: `POST https://api.kie.ai/api/v1/jobs/createTask`
- Kie.ai page: https://kie.ai/seedream
