# First Transaction

Obtain TURK from a source you trust and verify the receiving address. Select Turkchain Mainnet (`1919`) in the wallet. Start with a small transfer to an address you control.

Enter the recipient and amount, review gas and total cost, and confirm once. Save the hash returned by the wallet. Search it on TurkScan® and wait for a successful receipt. A pending transaction is not yet proof of payment.

If the explorer cannot find it, query `eth_getTransactionReceipt` on the RPC and check the selected network. Do not resend automatically: this can create a second payment. A failed transaction can still consume gas; see [Failure Analysis](../transactions/failure-and-revert-analysis.md).
