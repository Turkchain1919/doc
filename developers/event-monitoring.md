# Event Monitoring

Choose the contract address and event ABI explicitly. Read logs over bounded block ranges or supported subscriptions; decode using the emitting contract's ABI.

Persist a checkpoint containing block number and block hash. Deduplicate by transaction hash and log index, reconcile canonical changes and backfill after a WebSocket reconnect. Advance checkpoints only after durable processing.

A subscription can disconnect or miss messages. Test `eth_subscribe` support on the configured endpoint before depending on it. Explorer logs are indexed data and may arrive later than RPC receipts. See [Logs API](../api-documentation/logs-api.md).
