# Native TURK Transfers

A native transfer sends TURK through a transaction's `value` in base units. Confirm the recipient supports native transfers; a contract can reject them.

Reserve additional TURK for gas. An ordinary account transfer often needs less gas than a contract invocation, but do not hard-code a gas limit when the recipient may contain code.

After signing, check the receipt's status and inspect the value and recipient on TurkScan®. Native movements inside contract execution may appear as [Internal Transactions](../accounts/internal-transactions.md).
