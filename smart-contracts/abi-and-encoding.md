---
description: '# ABI & Encoding'
---

# ABI & Encoding

```
The Application Binary Interface (ABI) defines how contract functions are encoded and decoded.
```

### Function Selector

```
## Function Selector
```

The first 4 bytes of call data represent the function selector.

It is calculated as:

keccak256("functionName(parameterTypes)")

### Example

Slash → /code 0xa9059cbb

```
Represents transfer(address,uint256)
```

