# Token Allowances and Approvals

An ERC-20 approval grants a spender permission under the token contract's rules. It is not a swap, bridge dispatch or liquidity deposit. An NFT operator approval can have a different scope.

## What to check

Inspect the token, spender, allowance and chain before signing. Bound the approval when practical and review unused permissions through a trusted interface. Retain separate hashes for approval and the later application action.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/tokens/erc-20-tokens). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
