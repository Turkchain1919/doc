# API Integration

Use `https://turkscan.com/api/v2` for indexed explorer REST data and `https://rpc.turkscan.com` for node JSON-RPC. They have different request formats, pagination and error semantics.

```javascript
const response = await fetch('https://turkscan.com/api/v2/stats');
if (!response.ok) throw new Error(`TurkScan HTTP ${response.status}`);
const stats = await response.json();
console.log(stats.total_blocks);
```

Respect timeouts and [rate limits](../api-documentation/rate-limits.md). Follow returned `next_page_params` and keep large numeric strings precise. Preserve null prices as unavailable. See the [endpoint reference](../api-documentation/introduction.md) for request parameters and captured responses.
