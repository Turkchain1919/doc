# Transaction Hash

An EVM transaction hash is `0x` followed by 64 hexadecimal characters. It identifies a signed transaction on a particular network and links its receipt, logs and indexed execution details.

A hash returned at submission is not proof of success. Wait for a receipt and inspect status. A wallet can replace a pending transaction using the same nonce; the replacement has a different hash.

Copy the full hash when requesting help. Never share a seed phrase or private key. Use [Transactions API](../api-documentation/transactions-api.md) for machine access.
