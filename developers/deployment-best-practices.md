# Solidity Development and Contract Deployment

Compile and test locally using pinned compiler and dependency versions. Retain the compiler Standard JSON Input, metadata and deployment artifacts. Confirm the intended EVM target against the node rather than assuming the newest opcode set is available.

Before mainnet deployment, confirm chain ID `1919`, signer address, constructor values, library links and TURK balance. Simulate deployment when supported and review gas costs. After broadcast, wait for a successful receipt and check code at the resulting address.

Publish source through [contract verification](../smart-contracts/contract-verification.md). For upgradeable systems, verify both proxy and implementation and record initialization and administrator roles. No example here deploys or signs automatically.
