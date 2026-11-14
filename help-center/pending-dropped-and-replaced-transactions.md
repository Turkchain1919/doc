# Pending, Dropped and Replaced Transactions

A pending transaction has not yet been included. A node can stop retaining it, and a wallet can replace a transaction using the same sender and nonce. A replacement has its own hash.

## What to check

Check both hashes and the sender nonce on the correct network. Use the wallet's documented replacement workflow only after understanding its fee policy. A dropped explorer record is not evidence that no node can still include the transaction.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/transactions/transaction-status). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
