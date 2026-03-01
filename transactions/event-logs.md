---
description: '# Event Logs'
---

# Event Logs

```
Event logs are generated when a smart contract emits events during execution.
```

### Log Structure

```
Each log contains:

• Contract address  
• Topics (indexed parameters)  
• Data (non-indexed parameters)  
• Block number  
• Transaction hash  
```

### ERC-20 Transfer Example

```
event Transfer(address indexed from, address indexed to, uint256 value);
```
