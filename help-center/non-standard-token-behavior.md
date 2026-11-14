# Non-Standard Token Behavior

Transfer fees, rebasing, unusual return values and custom balance rules can make a token behave differently from a simple ERC-20. Explorer event totals may not equal an application's expected received amount.

## What to check

Check the verified code, actual balance changes and receipt logs. Use token-specific decimals and account for transfer fees in integrations. Do not report a fixed 1:1 received amount without checking the contract.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/tokens/token-metadata-and-supply-analytics). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
