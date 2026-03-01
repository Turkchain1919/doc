---
description: '# API Introduction'
---

# Introduction

The TurkScan API provides programmatic access to Turkchain blockchain data.

It follows an Etherscan-compatible structure for seamless integration.

### Base Endpoint

### Base URL

[https://api.turkscan.com/api](https://api.turkscan.com/api)

### Request Format

```
// Some code
https://api.turkscan.com/api
   ?module=account
   &action=balance
   &address=0x...
   &tag=latest
   &apikey=YourApiKey
```

### Response Format

```
All responses are returned in JSON format.
```
