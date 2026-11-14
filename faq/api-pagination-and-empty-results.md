# API Pagination and Empty Results

V2 lists commonly return items and next_page_params. An empty list can be legitimate. The compatibility API can use status 0 with an empty result even on HTTP 200.

## What to check

Keep the original filter, pass the returned cursor to the same resource and stop when it is null. Deduplicate identifiers when retrying. Do not invent missing activity or treat every empty result as a broken network.

## Further guidance

[Read the detailed TurkScan guide](../api-documentation/pagination.md). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
