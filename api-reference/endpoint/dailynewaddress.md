# TurkScan® Daily New Addresses

The current address directory is not automatically a daily first-seen series. A historical metric needs durable first-seen indexing and a clear definition of account creation.

**Verified counterpart:** GET `https://turkscan.com/api/v2/addresses`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses'
```

```json
{
  "items": [
    {
      "transactions_count": "659",
      "coin_balance": "99997698655729057944103675546",
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
    }
  ],
  "total_supply": "0",
  "next_page_params": {
    "hash": "0x1b33c89e9b81fbbbe14aab6df0b78fe5af5dbac5",
    "transactions_count": 4,
    "fetched_coin_balance": "12000000000"
  },
  "exchange_rate": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
