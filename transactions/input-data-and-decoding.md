# Input Data & Decoding

Input data is the byte sequence supplied to contract execution. A typical ABI-encoded call begins with a 4-byte function selector followed by encoded arguments. Native transfers to ordinary accounts can have empty input.

TurkScan® attempts to decode methods using available ABI or signatures. A selector match alone is not proof that the called contract implements the expected behavior. Always verify the contract address and implementation.

Unknown input can still be inspected as raw hex. See [ABI & Encoding](../smart-contracts/abi-and-encoding.md).
