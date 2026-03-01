---
description: '# Failure & Revert Analysis'
---

# Failure & Revert Analysis

```
A transaction may fail due to execution errors.
```

### Common Failure Reasons

```
• Out of Gas  
• Revert()  
• Require condition not met  
• Invalid opcode  
• Insufficient balance  
```

### Revert Message

```
## Revert Messages
```

```
If the contract emits a revert reason string, TurkScan displays it for easier debugging.
```

### Debugging Tips

```
To debug failed transactions:

1. Check revert message  
2. Inspect input data  
3. Verify gas limit  
4. Simulate transaction locally  
```
