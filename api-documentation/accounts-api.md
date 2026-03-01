---
description: '# Accounts API'
---

# Accounts API

```
Retrieve account balances and transaction lists.
```

### Get Balance

```
// Some code
module=account
action=balance
address=0x...
tag=latest
```

### Get Transaction List

```
module=account
action=txlist
address=0x...
startblock=0
endblock=99999999
sort=asc
```

### Get Token Transfers

```
module=account
action=tokentx
address=0x...
```
