---
description: '# Hardhat Setup'
---

# Hardhat Setup

```
Turkchain can be integrated into Hardhat as a custom network.
```

### Installation

```
// Some code
npm install --save-dev hardhat
```

hardhat.config.js

```
// Some code
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    turkchain: {
      url: "https://rpc.turkchain1919.com",
      chainId: 1919,
      accounts: ["PRIVATE_KEY"]
    }
  }
};
```

### Deploy Command

```
npx hardhat run scripts/deploy.js --network turkchain
```
