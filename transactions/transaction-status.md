# Transaction Status

**Pending:** observed but not yet included in an indexed block. Pending visibility depends on node and indexer support.

**Success:** the receipt reports successful top-level execution. Check the method and logs to understand what actually happened; a successful approval does not perform a swap or liquidity deposit.

**Failed:** execution reverted or ran out of gas. State changes are reverted according to EVM rules, but gas can still be charged.

**Not found:** the explorer has no indexed record. This is not itself a failed receipt. Verify chain ID and query the RPC before resubmitting. A replacement may share a sender and nonce but have a different hash.
