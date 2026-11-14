# API Key and Limit Problems

TurkScan credentials and operator limits are independent of other providers. A documented optional key parameter does not prove every resource uses the same policy.

## What to check

Use only a key from the supported TurkScan account workflow where available. Inspect 401/403 versus 429 separately and honor Retry-After when supplied. Do not expose keys in a public URL or send them with a help request.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/api-documentation/authentication-and-api-keys). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
