# Gas Fees

Gas measures EVM execution work. The gas limit caps how much the transaction may use; the effective gas price determines the cost per unit actually charged.

`execution fee = gas used × effective gas price`

Gas prices are often displayed in gwei (`10^9` base units). TURK has `10^18` base units. Use wallet estimation or `eth_estimateGas`; allow for changing state and never assume a fixed fee from a documentation example.

The explorer statistics endpoint exposes current gas estimates when available. It is not a guarantee of inclusion. See [Gas Mechanics](../transactions/gas-mechanics.md).
