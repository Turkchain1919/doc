# API Operation Availability

This is a complete inventory of the operations declared by the deployed OpenAPI snapshot, not an enabled-feature list. The specification includes optional and generic routes. Only observed successful requests are described as tested reads. Source verification submission routes are documented separately because they are absent from this generated contract.

| Method | Declared path | Audit evidence |
| --- | --- | --- |
| GET | `/api/legacy/block/get-block-number-by-time` | Not exercised |
| POST | `/api/legacy/eth/eth-block-number` | Not exercised; no state-changing request sent |
| POST | `/api/legacy/eth/eth-call` | Not exercised; no state-changing request sent |
| POST | `/api/legacy/eth/eth-get-balance` | Not exercised; no state-changing request sent |
| POST | `/api/legacy/eth/eth-get-logs` | Not exercised; no state-changing request sent |
| POST | `/api/legacy/eth/eth-get-storage-at` | Not exercised; no state-changing request sent |
| POST | `/api/legacy/eth/eth-send-raw-transaction` | Not exercised; no state-changing request sent |
| GET | `/api/v1/search` | Not exercised |
| GET | `/api/v2/addresses` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/blocks-validated` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/coin-balance-history` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/coin-balance-history-by-day` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/counters` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/internal-transactions` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/internal-transactions/csv` | Not exercised |
| GET | `/api/v2/addresses/{address_hash_param}/logs` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/logs/csv` | Not exercised |
| GET | `/api/v2/addresses/{address_hash_param}/nft` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/nft/collections` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/tabs-counters` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/token-balances` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/token-transfers` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/token-transfers/csv` | Not exercised |
| GET | `/api/v2/addresses/{address_hash_param}/tokens` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/transactions` | Observed HTTP 200 |
| GET | `/api/v2/addresses/{address_hash_param}/transactions/csv` | Not exercised |
| GET | `/api/v2/addresses/{address_hash_param}/withdrawals` | Not exercised; chain-specific support not established |
| GET | `/api/v2/advanced-filters` | Observed HTTP 200 |
| GET | `/api/v2/advanced-filters/csv` | Not exercised |
| GET | `/api/v2/advanced-filters/methods` | Observed HTTP 200 |
| GET | `/api/v2/blocks` | Observed HTTP 200 |
| GET | `/api/v2/blocks/{block_hash_or_number_param}` | Observed HTTP 200 |
| GET | `/api/v2/blocks/{block_hash_or_number_param}/internal-transactions` | Observed HTTP 200 |
| GET | `/api/v2/blocks/{block_hash_or_number_param}/transactions` | Observed HTTP 200 |
| GET | `/api/v2/blocks/{block_hash_or_number_param}/withdrawals` | Not exercised; chain-specific support not established |
| GET | `/api/v2/blocks/{block_number_param}/countdown` | Observed HTTP 404 |
| GET | `/api/v2/config/backend` | Observed HTTP 200 |
| GET | `/api/v2/config/backend-version` | Observed HTTP 200 |
| GET | `/api/v2/config/csv-export` | Not exercised |
| GET | `/api/v2/config/db-background-migrations` | Observed HTTP 200 |
| GET | `/api/v2/config/indexer` | Observed HTTP 200 |
| GET | `/api/v2/config/public-metrics` | Observed HTTP 200 |
| GET | `/api/v2/config/smart-contracts/languages` | Observed HTTP 200 |
| GET | `/api/v2/csv-exports/{uuid_param}` | Not exercised |
| GET | `/api/v2/internal-transactions` | Observed HTTP 200 |
| GET | `/api/v2/main-page/blocks` | Observed HTTP 200 |
| GET | `/api/v2/main-page/indexing-status` | Observed HTTP 200 |
| GET | `/api/v2/main-page/transactions` | Observed HTTP 200 |
| GET | `/api/v2/main-page/transactions/watchlist` | Not exercised |
| GET | `/api/v2/proxy/account-abstraction/accounts` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/accounts/{address_hash_param}` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/bundlers` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/bundlers/{address_hash_param}` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/bundles` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/factories` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/factories/{address_hash_param}` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/operations` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/operations/{operation_hash_param}` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/operations/{operation_hash_param}/summary` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/paymasters` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/paymasters/{address_hash_param}` | Not exercised; bundler service not established |
| GET | `/api/v2/proxy/account-abstraction/status` | Not exercised; bundler service not established |
| GET | `/api/v2/search` | Observed HTTP 200 |
| GET | `/api/v2/search/check-redirect` | Observed HTTP 200 |
| GET | `/api/v2/search/quick` | Observed HTTP 200 |
| GET | `/api/v2/shibarium/deposits` | Not exercised; chain-specific support not established |
| GET | `/api/v2/shibarium/deposits/count` | Not exercised; chain-specific support not established |
| GET | `/api/v2/shibarium/withdrawals` | Not exercised; chain-specific support not established |
| GET | `/api/v2/shibarium/withdrawals/count` | Not exercised; chain-specific support not established |
| GET | `/api/v2/smart-contracts/` | Observed HTTP 200 |
| GET | `/api/v2/smart-contracts/counters` | Observed HTTP 200 |
| GET | `/api/v2/smart-contracts/{address_hash_param}` | Observed HTTP 200 |
| GET | `/api/v2/smart-contracts/{address_hash_param}/audit-reports` | Observed HTTP 200 |
| POST | `/api/v2/smart-contracts/{address_hash_param}/audit-reports` | Not exercised; no state-changing request sent |
| GET | `/api/v2/stats` | Observed HTTP 200 |
| GET | `/api/v2/stats/charts/market` | Observed HTTP 200 |
| GET | `/api/v2/stats/charts/secondary-coin-market` | Observed HTTP 200 |
| GET | `/api/v2/stats/charts/transactions` | Observed HTTP 200 |
| GET | `/api/v2/stats/hot-smart-contracts` | Observed HTTP 422 |
| GET | `/api/v2/token-transfers` | Observed HTTP 200 |
| GET | `/api/v2/tokens/` | Observed HTTP 200 |
| POST | `/api/v2/tokens/batch` | Not exercised; no state-changing request sent |
| GET | `/api/v2/tokens/{address_hash_param}` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/counters` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/holders` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/holders/csv` | Not exercised |
| GET | `/api/v2/tokens/{address_hash_param}/instances` | Observed HTTP 200 |
| PATCH | `/api/v2/tokens/{address_hash_param}/instances/refetch-metadata` | Not exercised; no state-changing request sent |
| GET | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/holders` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/media-type` | Not exercised |
| PATCH | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/refetch-metadata` | Not exercised; no state-changing request sent |
| GET | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/transfers` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/transfers-count` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/transfers` | Observed HTTP 200 |
| GET | `/api/v2/tokens/{address_hash_param}/transfers/csv` | Not exercised |
| GET | `/api/v2/tokens/{address_hash_param}/ui-multiplier-changes` | Not exercised |
| GET | `/api/v2/transactions` | Observed HTTP 200 |
| GET | `/api/v2/transactions/stats` | Observed HTTP 200 |
| GET | `/api/v2/transactions/watchlist` | Not exercised |
| GET | `/api/v2/transactions/{transaction_hash_param}` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/external-transactions` | Observed HTTP 404 |
| GET | `/api/v2/transactions/{transaction_hash_param}/fhe-operations` | Not exercised; chain-specific support not established |
| GET | `/api/v2/transactions/{transaction_hash_param}/internal-transactions` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/logs` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/preview` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/raw-trace` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/state-changes` | Observed HTTP 200 |
| GET | `/api/v2/transactions/{transaction_hash_param}/summary` | Observed HTTP 403 |
| GET | `/api/v2/transactions/{transaction_hash_param}/token-transfers` | Observed HTTP 200 |
| GET | `/api/v2/validators/stability` | Not exercised; chain-specific support not established |
| GET | `/api/v2/validators/stability/counters` | Not exercised; chain-specific support not established |
| GET | `/api/v2/withdrawals` | Not exercised; chain-specific support not established |
| GET | `/api/v2/withdrawals/counters` | Not exercised; chain-specific support not established |

See [Contract Verification API](contract-verification-api.md) and [Complete evidence](../reference/endpoint-evidence.json).

A follow-up future-height countdown test succeeded for both API formats. The original current/mined-height error remains recorded. See [Countdown](endpoint/getblockcountdown.md).
