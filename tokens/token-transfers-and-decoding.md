---
description: '# Token Transfers & Decoding'
---

# Token Transfers & Decoding

Token transfers are identified by parsing smart contract event logs.

### How Detection Works

```
1. Contract emits Transfer event  
2. Event signature is matched  
3. Parameters are decoded  
4. Transfer is indexed in database  
```

### ERC-20 Transfer Example

```
Topics[0] = keccak256("Transfer(address,address,uint256)")
```

