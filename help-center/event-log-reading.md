# Reading Event Logs

Logs contain an emitting contract, topics and data. One transaction can emit many events, and a familiar Transfer signature can be produced by an untrusted token.

## What to check

Confirm the contract address and receipt status, then decode with its ABI. Deduplicate by transaction hash and log index in integrations. An indexed event is different from a separately signed transaction.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/transactions/event-logs). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
