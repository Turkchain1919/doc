# Error Handling

Inspect HTTP status and the JSON body together.

| Observation | Meaning / action |
| --- | --- |
| 200 with V2 JSON | Decode the resource; lists can legitimately be empty |
| 400 unknown action/module | Wrong route or unsupported compatibility action |
| 403 | Restricted or disabled feature; do not retry as a successful endpoint |
| 404 | Missing indexed resource or unavailable route; check identifier and deployment |
| 422 | Invalid input or a route's unmet query requirements |
| 429 | Back off and honor `Retry-After` when present |
| 5xx | Transient or persistent service fault; bounded retries for safe reads |

A malformed address returned 422 and a well-formed unknown transaction returned 404 in live probes. Transaction summary returned 403. Actual bodies are in the endpoint reference.

Compatibility responses use `status`, `message` and `result`; HTTP 200 with `status: "0"` can describe an empty search or application error. Node JSON-RPC uses a separate `error` object. Do not treat all three formats as interchangeable.
