# TurkScan® Daily Block Counts

For a daily count, define a UTC window and traverse canonical indexed blocks in that interval. A list endpoint is not itself a precomputed daily analytics API.

**Verified counterpart:** GET `https://turkscan.com/api/v2/blocks`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks'
```

```json
{
  "items": [
    {
      "base_fee_per_gas": "1000000000",
      "burnt_fees": "0",
      "burnt_fees_percentage": null,
      "difficulty": "0",
      "gas_limit": "4294967295",
      "gas_target_percentage": -100.0,
      "gas_used": "0",
      "gas_used_percentage": 0.0,
      "hash": "0x5a45faca9a8c98fe652affa072a9827bb6c396a0ca478e4f7b1d51fb3415adc8",
      "height": 3142006,
      "internal_transactions_count": null,
      "is_pending_update": false,
      "miner": {
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
      "nonce": "0x0000000000000000",
      "parent_hash": "0x971e406f94869dc2c7b013e657f1914474bb380818bc0318986bee8a2623a8b7",
      "priority_fee": "0",
      "rewards": [],
      "size": 619,
      "timestamp": "2026-11-14T08:52:13.000000Z",
      "total_difficulty": null,
      "transaction_fees": "0",
      "transactions_count": 0,
      "type": "block",
      "uncles_hashes": [],
      "withdrawals_count": null
    }
  ],
  "next_page_params": {
    "block_number": 3141957
  }
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
