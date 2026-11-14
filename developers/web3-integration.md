# Web3 Development

EVM clients can connect through the mainnet JSON-RPC endpoint. Define chain `1919` explicitly, use TURK with 18 decimals for native value, and use each contract's own decimals for token amounts.

Use typed ABI calls and big integers. Separate public read clients from wallet signing clients; a public RPC endpoint does not provide access to user keys. Verify the connected wallet chain before every write.

See [Viem](viem-integration.md), [Ethers.js](ethers-integration.md), [MetaMask](metamask-integration.md), [API Integration](api-integration.md) and [Event Monitoring](event-monitoring.md).
