# TurkScan® Contract Creation Data

**Method:** GET. **URL:** `https://turkscan.com/api?module=contract&action=getcontractcreation&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

**Purpose:** Read contract verification or deployment data.

**Parameters and required fields:** `module=contract` and `action=getcontractcreation` are required. Required: `contractaddresses` as a comma-separated list of contract addresses.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=contract&action=getcontractcreation&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "blockNumber": "2970579",
      "contractAddress": "0xbf9569b06bcb6ccf776302b0697c79b8407d8e3f",
      "contractCreator": "0x8b00ecb1e8bf59f5ab4ba0f0c528c4f4d850280e",
      "contractFactory": "",
      "creationBytecode": "0x6080604052604051610e03380380610e03833981016040819052610022916103f4565b828161003082826000610044565b5061003c905082610070565b505050610519565b61004d836100de565b60008251118061005a5750805b1561006b57610069838361011e565b505b505050565b7f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f6100b0600080516020610dbc833981519152546001600160a01b031690565b604080516001600160a01b03928316815291841660208301520160405180910390a16100db8161014a565b50565b6100e7816101e6565b6040516001600160a01b038216907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a250565b60606101438383604051806060016040528060278152602001610ddc6027913961027a565b9392505050565b6001600160a01b0381166101b45760405162 [excerpt]",
      "timestamp": "1793739669",
      "txHash": "0x1d9dba155e971db814e60f59e827b4d9fa98784dd6f3e29678d912ac18b62b8a"
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
