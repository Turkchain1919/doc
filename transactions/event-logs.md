# Logs and Events

Contracts emit logs containing the emitting address, indexed topics and non-indexed data. For a typical non-anonymous Solidity event, topic zero is the hash of its signature. Decode topics and data using the correct ABI.

A `Transfer` signature can be emitted by an untrusted contract. Confirm the emitting contract address and transaction receipt. Reverted execution does not retain its emitted logs in the successful receipt.

Query logs by transaction or address using the [Logs API](../api-documentation/logs-api.md). Use transaction hash plus log index to identify an event, and handle reorgs or indexer corrections in integrations.
