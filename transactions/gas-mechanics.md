# Gas Mechanics

The gas limit is an execution cap; gas used is actual consumed work reported by the receipt. Effective gas price is the price paid per unit. The explorer's fee represents the charged execution cost in TURK.

For receipts with `gasUsed` and `effectiveGasPrice`, multiply those integers to obtain base units, then divide by `10^18` for TURK. Decode JSON-RPC hexadecimal quantities before arithmetic. Do not confuse the sender's maximum fee setting with the actual fee.

Failed execution may still cost gas. `eth_estimateGas` is a simulation against current state, not a reservation or guarantee. See [Gas Strategy](../developers/gas-strategy.md).
