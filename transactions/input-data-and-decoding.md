---
description: '# Input Data & Decoding'
---

# Input Data & Decoding

```
Input data contains the function selector and encoded parameters of a smart contract call.
```

### ABI Decoding

```
## ABI Decoding
```

```
When a contract is verified, TurkScan decodes input data into readable function calls.
```

Example

```
0xa9059cbb000000000000000000000000...
```

Decoded as:

transfer(address recipient, uint256 amount)

