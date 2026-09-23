---
description: '# Foundry Setup'
---

# Foundry Setup

```
Turkchain is fully compatible with Foundry.
```

### foundry.toml

```
// Some code
[rpc_endpoints]
turkchain = "https://rpc.turkscan.com"
```

### Deploy with Forge

```
forge create src/Contract.sol:Contract \
  --rpc-url https://rpc.turkscan.com \
  --private-key YOUR_PRIVATE_KEY
```

### Verify Contract

```
// Some code
forge verify-contract \
  --chain-id 1919 \
  --compiler-version v0.8.20 \
  CONTRACT_ADDRESS \
  src/Contract.sol:Contract \
  YOUR_API_KEY
```
