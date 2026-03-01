---
description: '# ERC-20 Tokens'
---

# ERC-20 Tokens

```
ERC-20 is the standard for fungible tokens on Turkchain.
```

```
function totalSupply() public view returns (uint256);
function balanceOf(address account) public view returns (uint256);
function transfer(address recipient, uint256 amount) public returns (bool);
function approve(address spender, uint256 amount) public returns (bool);
function transferFrom(address sender, address recipient, uint256 amount) public returns (bool);
```

### ERC-20 Events

```
event Transfer(address indexed from, address indexed to, uint256 value);
event Approval(address indexed owner, address indexed spender, uint256 value);
```

TurkScan automatically decodes ERC-20 Transfer and Approval events.

### Supply & Holders

```
## Supply & Holder Tracking
```

TurkScan tracks:

• Circulating supply\
• Total supply\
• Holder distribution\
• Top holders list\
• Token transfer history
