# Internal Transactions

Internal transactions describe calls and native-value movements made during EVM execution. They are not independently signed transactions and do not have a separate transaction hash or nonce.

Open the parent transaction to inspect its status, call destination and available trace. A trace can contain reverted subcalls; do not count every listed value movement as a successful transfer.

Trace availability depends on node support and indexing. An empty internal-transactions list does not prove that a contract made no calls. See [Transactions API](../api-documentation/transactions-api.md).
