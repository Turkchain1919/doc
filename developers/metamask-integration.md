# MetaMask Integration

Request network addition from a user-initiated action:

```javascript
await window.ethereum.request({
  method: 'wallet_addEthereumChain',
  params: [{
    chainId: '0x77f',
    chainName: 'Turkchain Mainnet',
    nativeCurrency: { name: 'TURK', symbol: 'TURK', decimals: 18 },
    rpcUrls: ['https://rpc.turkscan.com'],
    blockExplorerUrls: ['https://turkscan.com'],
  }],
});
```

Handle rejection and wallets that do not implement this method. Use `wallet_switchEthereumChain` to request switching to `0x77f`, then read `eth_chainId` to confirm. Listen for account and chain changes and invalidate stale transaction drafts. A provider object must be present before calling it.
