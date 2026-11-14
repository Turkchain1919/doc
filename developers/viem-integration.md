# Viem Integration

This example targets Viem 2's public read-client API:

```typescript
import { createPublicClient, defineChain, http } from 'viem';

export const turkchain = defineChain({
  id: 1919,
  name: 'Turkchain Mainnet',
  nativeCurrency: { name: 'TURK', symbol: 'TURK', decimals: 18 },
  rpcUrls: { default: { http: ['https://rpc.turkscan.com'] } },
  blockExplorers: { default: { name: 'TurkScan', url: 'https://turkscan.com' } },
});
const client = createPublicClient({ chain: turkchain, transport: http() });
console.log(await client.getChainId()); // 1919
console.log(await client.getBlockNumber());
```

Pin the package version. Keep balances as `bigint` until formatting. Use a separate wallet client for writes, simulate supported contract calls and verify the wallet's chain. This snippet only reads public data.
