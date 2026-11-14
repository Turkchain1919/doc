# Native TURK

TURK is Turkchain® Mainnet's native execution currency. One TURK is `10^18` base units. Native transfers use a transaction's `value` field; they do not call an ERC-20 `transfer` function.

Use integer arithmetic for base units. A wallet needs sufficient TURK for both the transferred value and execution fees. An ERC-20 balance cannot automatically pay native gas.

See [Native TURK Transfers](../getting-started/native-turk-transfers.md) and [Wrapped TURK](../tokens/wrapped-turk.md).
