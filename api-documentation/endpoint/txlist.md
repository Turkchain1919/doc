# TurkScan® Address Transaction History

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=txlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=txlist` are required. Required: `address`. Optional `startblock`, `endblock`, `page`, `offset`, `sort` (`asc` or `desc`).

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=txlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "blockHash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
      "blockNumber": "3117475",
      "confirmations": "24660",
      "contractAddress": "",
      "cumulativeGasUsed": "175465",
      "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
      "gas": "260611",
      "gasPrice": "1000100000",
      "gasUsed": "175465",
      "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
      "isError": "0",
      "methodId": "0x7c39d130",
      "nonce": "2",
      "timeStamp": "1794518361",
      "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
      "transactionIndex": "0",
      "txreceipt_status": "1",
      "value": "0"
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
