# Gas Strategy

Estimate the intended call with its real sender, recipient, value and calldata. Check native TURK balance covers value plus gas. Use integer arithmetic and preserve the distinction between gas units, gwei and TURK.

Set bounded fee policies appropriate to your application. A gas estimate can fail because the call reverts; increasing the limit does not fix a missing approval, expired deadline or access restriction.

Track pending nonces and receipt status. Do not submit repeated transactions just because an explorer has not indexed the first one. See [Gas Mechanics](../transactions/gas-mechanics.md).
