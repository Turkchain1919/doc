# TurkScan® API Keys

Explorer account support is enabled. If the signed-in account UI offers API keys, create and manage them there. Treat generated values as secrets and avoid embedding them in browser bundles or public URLs that may be logged.

The audited public REST read calls succeeded without an API key. The OpenAPI contract lists optional `apikey` fields, but this does not prove every route uses identical authentication or rate policies. The operator-only `key` parameter is not a public credential to request or publish.

See [Authentication and API Keys](../../api-documentation/authentication-and-api-keys.md) and [Rate Limits](../../api-documentation/rate-limits.md).
