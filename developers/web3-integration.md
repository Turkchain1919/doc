---
description: '# Web3 Integration'
---

# Web3 Integration

```
Turkchain supports standard Web3 libraries.
```

### Ethers.js Example

```
// Some code
import { ethers } from "ethers";

const provider = new ethers.JsonRpcProvider(
  "https://rpc.turkchain1919.com"
);

const blockNumber = await provider.getBlockNumber();
console.log(blockNumber);
```

### Send Transaction

```
// Some code
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

const tx = await wallet.sendTransaction({
  to: "0xRecipientAddress",
  value: ethers.parseEther("1.0")
});

await tx.wait();
```

### Web3.js Example

```
// Some code
const Web3 = require("web3");
const web3 = new Web3("https://rpc.turkchain1919.com");

const block = await web3.eth.getBlockNumber();
console.log(block);
```
