# ERC-20 Tokens

ERC-20 defines fungible token interfaces such as `balanceOf`, `transfer`, `approve` and `allowance`. Each contract defines its own decimals and supply behavior; do not assume 18 decimals for every token.

An approval permits a spender to transfer tokens subject to the contract's rules. It is not itself a payment or swap. Review spender and amount and revoke unused approvals through a trusted interface when appropriate.

TurkScan® exposes indexed holders, transfers and metadata. Fee-on-transfer, rebasing or non-standard contracts may need special accounting. Verify balances directly when indexed data is delayed.
