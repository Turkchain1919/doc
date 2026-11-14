# DApp Development

Separate public reads from wallet requests. Validate chain ID, account, contract address, ABI and amount units before creating a transaction. Refresh drafts when accounts or chains change.

Show pending, successful, failed and rejected states distinctly. Keep the hash after broadcast and reconcile its receipt rather than relying on a modal closing. An approval transaction and the application action are separate steps.

Use API pagination, timeouts and durable event indexing. Treat token metadata and URLs as untrusted input. Do not manufacture a price, APR, liquidity value or bridge delivery status when the supporting data is unavailable.
