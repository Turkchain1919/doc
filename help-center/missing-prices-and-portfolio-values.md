# Missing Prices and Portfolio Values

A token balance can be correct while its fiat price is unavailable. Null price, volume or market-cap values mean that a verified quote is missing, not that the asset is worth zero.

## What to check

Check native/token units and the exact contract. Do not multiply by an untrusted token quote to produce a portfolio value. Keep unavailable monetary fields unavailable in exports and dashboards.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/network-statistics/supply-metrics). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
