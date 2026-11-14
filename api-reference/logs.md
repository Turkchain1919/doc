# Logs API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/addresses/{address_hash_param}/logs`

Read indexed address records — logs.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/logs`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `topic` | query | no | string; pattern `^0x([A-Fa-f0-9]*)$` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |
| `index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/logs'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/logs`

Read indexed transactions — logs.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/logs`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `items_count` | query | no | integer; min 1 |
| `index` | query | no | integer |
| `block_number` | query | no | integer; min 0 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/logs'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "address": {
        "ens_domain_name": null,
        "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
        "implementations": [
          {
            "address_hash": "0x648C7F1bBef585b36bc1f21Fc28e60fa27935545",
            "name": null
          }
        ],
        "is_contract": true,
        "is_scam": false,
        "is_verified": false,
        "metadata": {
          "reputation": null,
          "tags": []
        },
        "name": null,
        "private_tags": [],
        "proxy_type": "eip1967",
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "block_hash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
      "block_number": 3117475,
      "block_timestamp": "2026-11-12T21:19:21.000000Z",
      "data": "0x",
      "decoded": {
        "abi": null,
        "method_call": "Process(uint32 indexed origin, bytes32 indexed sender, address indexed recipient)",
        "method_id": "0d381c2a",
        "parameters": [
          {
            "indexed": true,
            "name": "origin",
            "type": "uint32",
            "value": "1"
          }
        ]
      },
      "index": 0,
      "smart_contract": {
        "ens_domain_name": null,
        "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": null,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "topics": [
        "0x0d381c2a574ae8f04e213db7cfb4df8df712cdbd427d9868ffef380660ca6574"
      ],
      "transaction_hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4"
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
