# Solidity and Contract Verification

Verification compares submitted compiler inputs with deployed bytecode. Preserve the exact Solidity version, optimizer configuration, EVM target, linked libraries, constructor arguments and source files used for deployment.

Open the contract on TurkScan® and choose Verify & Publish where available. Prefer Standard JSON Input for multi-file projects. The live verification configuration reports the Rust verifier enabled; enabled languages and compiler choices must be taken from that configuration rather than assumed.

The audit read verification configuration and verified contract data but did not submit source or deploy a contract. Vyper support must not be inferred from the presence of generic routes. See [Verification API](../api-documentation/contract-verification-api.md), [Foundry](../devs/verification/foundry-verification.md) and [Hardhat](../devs/verification/hardhat-verification-plugin.md).

Verified source establishes a source/bytecode match, not ownership, safety or freedom from upgrade risk.
