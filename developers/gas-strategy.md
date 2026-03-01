---
description: '# Gas Strategy'
---

# Gas Strategy

```
Gas optimization is critical for cost-efficient smart contract deployment and interaction.
```

### Recommended Approach

```
• Query eth_gasPrice before sending transactions  
• Avoid hardcoding gas price  
• Estimate gas before execution  
```

### Gas Estimation Example

```
// Some code
const estimatedGas = await contract.method().estimateGas();
```

### Congestion Strategy

```
During network congestion:

• Increase gas price moderately  
• Avoid excessive gas limit  
• Retry with replacement transaction if needed  
```
