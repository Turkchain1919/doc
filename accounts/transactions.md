# Account Transactions

The Transactions tab lists indexed outer transactions involving the address. Token Transfers and Internal Transactions provide related execution data and can contain multiple entries for one parent transaction.

Use the parent hash to deduplicate activity when calculating transaction counts. Include only successful receipts when reporting completed payments, and account for failed transactions when calculating gas expenditure.

See [Transactions](../transactions/transaction-overview.md) and the [Address API](../api-documentation/addresses-api.md).
