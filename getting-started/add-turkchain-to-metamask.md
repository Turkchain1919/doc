# Add Turkchain® to MetaMask

In MetaMask, open the network selector and choose the option to add a custom network. Enter:

| Setting | Value |
| --- | --- |
| Network | Turkchain® Mainnet |
| Chain ID (decimal) | `1919` |
| EVM chain ID (hex) | `0x77f` |
| Native currency | TURK |
| Decimals | `18` |
| HTTPS JSON-RPC | `https://rpc.turkscan.com` |
| WebSocket | `wss://evm-ws.turkscan.com` |
| Explorer | `https://turkscan.com` |

`eth_chainId` returned `0x77f` during the 14 November 2026 audit. Wallet network names are display labels; the chain ID determines the execution network.

Save and switch to Turkchain Mainnet. Confirm the wallet shows TURK. If the network already exists, inspect its RPC and chain ID rather than creating a conflicting entry. Adding a network never requires a seed phrase or private key.

For a DApp, use `wallet_addEthereumChain` with `chainId: '0x77f'` and then `wallet_switchEthereumChain`. Handle user rejection and unsupported wallet methods. See [MetaMask Integration](../developers/metamask-integration.md).
