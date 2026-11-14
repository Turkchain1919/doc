# Request and Response Examples

Read-only resource request:

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/backend-version'
```

Observed response:

```json
{"backend_version":"12.0.1"}
```

Search request:

```bash
curl --get --data-urlencode 'q=TURK' 'https://turkscan.com/api/v2/search'
```

See [Search API](search-api.md) for a captured response. Each category reference contains exact tested URLs and response snapshots. Examples may select only the first item of a list for readability; complete captures remain in [audit evidence](../reference/endpoint-evidence.json).

Use [Pagination](pagination.md), [Authentication](authentication-and-api-keys.md) and [Errors](error-handling.md) in real clients. No example includes a production private key or signs a transaction.
