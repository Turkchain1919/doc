# Ethers.js Integration

This example uses Ethers 6:

```javascript
import { JsonRpcProvider, formatEther } from 'ethers';

const provider = new JsonRpcProvider('https://rpc.turkscan.com');
const network = await provider.getNetwork();
if (network.chainId !== 1919n) throw new Error('Unexpected network');
console.log(await provider.getBlockNumber());
// Supply a validated address owned by your application or user:
// console.log(formatEther(await provider.getBalance(address)));
```

`formatEther` converts an 18-decimal native amount; it does not imply that Turkchain's currency is ETH. Display the result as TURK. Use `formatUnits` with the actual decimals for ERC-20 assets. A provider reads data; writing requires a signer and explicit user authorization.
