# TurkScan® JSON-RPC Examples

For network JSON-RPC, send POST requests to `https://rpc.turkscan.com`. Start with `eth_chainId` and confirm `0x77f`. See [Using RPC](../../../getting-started/using-rpc.md) for the full request and response.

The explorer's compatibility and legacy endpoints are distinct from the node RPC. In the audit, the Etherscan-style `module=proxy&action=eth_blockNumber` request returned HTTP 400 `Unknown module`; use the network RPC for that operation.

Do not assume every upstream debug, archive or subscription method is enabled. See [RPC Integration](../../../developers/rpc-integration.md).
