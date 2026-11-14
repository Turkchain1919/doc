# TurkScan® Advanced Address Transaction History

TurkScan® exposes an indexed advanced-filter resource at `https://turkscan.com/api/v2/advanced-filters`. The basic unfiltered read returned HTTP 200. Parameter names and combinations must come from the deployed schema, not from another provider's similarly named action.

For address transaction history, start with the [dedicated txlist guide](txlist.md) and then apply supported V2 direction, address and token filters from [Configuration and Indexed Data API](../configuration-api.md). Preserve the returned cursor and deduplicate parent transaction hashes when combining token and internal-call rows.

The audit did not exercise every filter combination. A successful unfiltered response is not evidence that arbitrary external query parameters are accepted. Empty results must remain empty and must not be converted into fabricated activity.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
