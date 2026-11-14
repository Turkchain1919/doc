# TurkScan® Token Holder List

The holder list is paginated indexed data. Preserve the returned cursor and compare critical balances with the contract at a known block.

**Verified counterpart:** GET `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/holders`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/holders'
```

```json
{
  "items": [
    {
      "address": {
        "ens_domain_name": null,
        "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": {
          "reputation": null,
          "tags": []
        },
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "token_id": null,
      "value": "557348745844634010031909"
    }
  ],
  "next_page_params": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
