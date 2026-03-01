---
description: '# Contract Verification'
---

# Contract Verification

```
Contract verification ensures the published source code matches the deployed bytecode on Turkchain.
```

### Verification Process

```
## Verification Steps
```

1. Submit Solidity source code
2. Select compiler version
3. Set optimization settings
4. Provide constructor arguments
5. Submit for compilation
6. Bytecode comparison is performed

### Matching Logic

```
## Bytecode Matching
```

TurkScan recompiles the submitted source code.

If the resulting bytecode matches the deployed on-chain bytecode, the contract is marked as Verified.

### Required Parameters

```
• Compiler version  
• Optimization enabled / disabled  
• Optimization runs  
• EVM version (if specified)  
• Constructor arguments  
```
