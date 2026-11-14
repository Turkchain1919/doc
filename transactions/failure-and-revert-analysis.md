# Failed Transactions and Troubleshooting

Find the transaction hash on TurkScan® and check receipt status before retrying. Common causes include insufficient native TURK for value and gas, a reverted contract condition, expired deadline, missing token allowance, wrong network or out-of-gas execution.

Inspect available revert data, input arguments and internal calls. A contract's custom error requires its ABI to decode. A mined failure differs from a wallet rejecting a request before broadcast.

Reproduce using `eth_call` against appropriate historical state where supported. Archive state and full traces are not guaranteed by the public RPC. Fix the cause before signing a new transaction; never assume raising gas will bypass a contract's access control.
