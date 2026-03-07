# KIE Credit Budget Guard

The **KIE Credit Budget Guard** node acts as a gate in your ComfyUI workflows. Before an expensive generation node runs, this node checks the current credit balance via the Kie.ai API and only allows the workflow to continue if there are enough credits remaining.

This helps protect against accidentally running expensive batch workflows when low on credits.

## Inputs

| Name | Type | Description |
| :--- | :--- | :--- |
| **min_credits_required** | `INT` | The minimum credits needed to proceed. Default is `100`. |
| **passthrough** | `*` (Any) | An optional value to be passed through if the check passes. This allows the node to be chained inline in the middle of a workflow without disrupting data flow. |

## Outputs

| Name | Type | Description |
| :--- | :--- | :--- |
| **passthrough** | `*` (Any) | The same value passed through the input if credits are sufficient. |
| **credits_remaining** | `INT` | Your current credit balance via the Kie.ai API. |

## Behavior
- The node calls the Kie.ai credits endpoint (using the API key in `config/kie_key.txt` or the `KIE_API_KEY` environment variable).
- If `credits_remaining >= min_credits_required`, the node completes successfully, passing through the connected input and outputting the current balance.
- If `credits_remaining < min_credits_required`, the node raises a ComfyUI execution error with a clear message: `"Insufficient Kie.ai credits: X remaining, Y required. Workflow stopped."` This prevents downstream nodes from executing and consuming partial credits or returning failures.
