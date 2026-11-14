# RPC Integration and EVM Compatibility

Use `https://rpc.turkscan.com` for EVM JSON-RPC and `wss://evm-ws.turkscan.com` for supported WebSocket operations. Confirm `eth_chainId` equals `0x77f` before signing or sending.

Read methods return node state; TurkScan REST returns indexed explorer data. Use JSON-RPC `id` to associate responses and inspect the `error` object even when HTTP returns 200. Hexadecimal quantities and byte strings have different encoding rules.

Retry idempotent reads with bounded exponential backoff and timeouts. Do not blindly retry transaction submission as a new payment. Preserve the signed transaction hash and reconcile receipts. Public archive state, trace methods, filters and subscription capacity are not guaranteed unless separately tested.

For WebSockets, reconnect, resubscribe and backfill missed blocks over HTTP. Event subscriptions are not durable queues.
