# TurkScan® Contract ABI

**Method:** GET. **URL:** `https://turkscan.com/api?module=contract&action=getabi&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

**Purpose:** Read contract verification or deployment data.

**Parameters and required fields:** `module=contract` and `action=getabi` are required. Required: `address` of a verified contract. `result` is a JSON-encoded ABI string.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=contract&action=getabi&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_logic\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"admin_\",\"type\":\"address\"},{\"internalType\":\"bytes\",\"name\":\"_data\",\"type\":\"bytes\"}],\"stateMutability\":\"payable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"previousAdmin\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"newAdmin\",\"type\":\"address\"}],\"name\":\"AdminChanged\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"beacon\",\"type\":\"address\"}],\"name\":\"BeaconUpgraded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"implementa [excerpt]",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
