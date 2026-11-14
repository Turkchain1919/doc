# Advanced Search and Filtering

Exact addresses and hashes are more reliable than token names. V2 search and advanced-filter reads are available, but each filter must use the deployed contract's actual parameter names.

## What to check

Start from a known exact identifier, narrow the resource and preserve filters across pagination. Empty results can reflect the chosen scope or indexing delay. Do not combine token-transfer rows and parent transactions as though they were the same count.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/api-documentation/configuration-api). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
