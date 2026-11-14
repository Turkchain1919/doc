# TurkScan® Internal Calls by Block Range

The V2 resource returns indexed internal calls. Use its declared filters and returned cursor; do not append another provider's unsupported selectors. For deterministic block-scoped processing, use the block internal-transactions resource.

**Verified counterpart:** GET `https://turkscan.com/api/v2/internal-transactions`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/internal-transactions'
```

```json
{
  "items": [
    {
      "block_number": 2604265,
      "created_contract": {
        "ens_domain_name": null,
        "hash": "0x98aeecA4A7e4D0801Ccd2F69ae26D2Ae31bd0C15",
        "implementations": [],
        "is_contract": true,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "error": null,
      "from": {
        "ens_domain_name": null,
        "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "gas_limit": "1733110",
      "index": 0,
      "success": true,
      "timestamp": "2026-10-12T22:11:07.000000Z",
      "to": null,
      "transaction_hash": "0x4a62256c9e5e1e341ebae317fc461370d43e0387a2372e33aa93bd4fc7b0b1cd",
      "transaction_index": 0,
      "type": "create",
      "value": "0"
    }
  ],
  "meta": {
    "message": null,
    "status": 1
  },
  "next_page_params": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
