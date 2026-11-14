# Hardhat Setup

Install a compatible Hardhat release and its EVM tooling in your own project. Pin versions in your lockfile and follow the installed release's configuration format; Hardhat major versions use different network and secret-management APIs.

Configure an HTTP network with URL `https://rpc.turkscan.com` and chain ID `1919`. Keep signer credentials in the tool's supported keystore or secret facility, outside version control. Confirm `eth_chainId` before deployment.

Compile with an explicitly selected Solidity version, optimizer settings and an EVM target supported by the node. Test locally first. Preserve build artifacts and Standard JSON Input for [verification](../devs/verification/hardhat-verification-plugin.md).

No deployment is performed by reading these instructions. Mainnet deployment spends real TURK.
