# API Compatibility Matrix

Etherscan's documentation was used to compare category coverage, not copied or rebranded. Its hosted multichain API V2, subscription tiers and chain support list are separate from TurkScan®.

| Category | Verified TurkScan counterpart | Limits / unsupported assumptions |
| --- | --- | --- |
| Accounts | Address V2; account balance, balancemulti, txlist and transfer actions | Historical selectors and all optional variants not exercised |
| Contracts | V2 contract detail; getabi, getsourcecode, getcontractcreation | Write/verification submissions inspected in source, not executed |
| Transactions | V2 detail, logs, traces; gettxinfo, gettxreceiptstatus, getstatus | Summary returned 403; external-transactions returned 404 |
| Blocks | V2 list/detail/transactions; getblockreward, getblocknobytime | Reward schema is not a validated monetary policy |
| Tokens | V2 tokens/holders/transfers; tokenbalance, tokensupply | Ticker and icon do not establish an official asset |
| Logs | V2 address/transaction logs; logs/getLogs | Empty result is shown accurately; broad ranges not stress-tested |
| Gas | V2 stats gas estimates | `module=gastracker&action=gasoracle` returned 400 Unknown module |
| Statistics | V2 stats and charts; coinprice, ethprice, ethsupply | Prices were null; supply observations need validated methodology |
| Proxy | Network RPC provides node methods separately | `module=proxy&action=eth_blockNumber` returned 400 Unknown module |
| API V2 | TurkScan resource-oriented `/api/v2/*` | Not Etherscan `/v2/api?chainid=...`; no full parity claimed |
| Authentication | Tested public reads without key; account support enabled | Etherscan keys/plans are not TurkScan credentials/plans |
| Rate limits | Handle HTTP 429 and bounded retry | No contractual quota verified |
| Error codes | HTTP status + V2 body; compatibility status envelope | Do not import another provider's full error-code catalog |
| NFT | ERC-721 instance reads tested with indexed data; ERC-1155 filter returned empty | Empty ERC-1155 index is not a tested asset deployment |

See the [operation availability inventory](availability.md) for all declared REST paths and the [tested compatibility requests](compatibility-api.md) for exact responses.
