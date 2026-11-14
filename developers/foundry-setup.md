# Foundry Setup

Create a Foundry project, pin the Solidity compiler and test contracts locally. Inspect the RPC chain before using a signer:

```bash
cast chain-id --rpc-url https://rpc.turkscan.com
```

Expected chain ID: `1919`. Use Foundry's supported encrypted keystore or hardware wallet. Do not put private keys in shell history, source files or documentation.

Preserve compiler settings, linked libraries and constructor arguments. Deployment scripts should first simulate against the intended state. Review estimated gas and target addresses before broadcasting. See [Foundry Verification](../devs/verification/foundry-verification.md).
