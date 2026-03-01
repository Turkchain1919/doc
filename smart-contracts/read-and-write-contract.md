---
description: '# Read & Write Contract'
---

# Read & Write Contract

```
Verified contracts expose their ABI, enabling direct interaction through TurkScan.
```

### Read Contract

```
## Read Contract
```

Read functions are view or pure functions that do not modify state.

These calls are executed locally and require no gas.

### Write Contract

```
## Write Contract
```

```
Write functions modify blockchain state and require a connected wallet and gas fee.
```

### Interaction Flow

```
Wallet → ABI Encoding → RPC → Validator Execution → State Update
```

