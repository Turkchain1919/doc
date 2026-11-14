# TurkScan® Block Transaction Count

Read the indexed block transaction count where present, or count the canonical block's transaction hashes from RPC. Empty blocks legitimately contain zero transactions.

**Verified counterpart:** GET `https://turkscan.com/api/v2/blocks/3141995`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3141995'
```

```json
{
  "base_fee_per_gas": "1000000000",
  "burnt_fees": "0",
  "burnt_fees_percentage": null,
  "difficulty": "0",
  "gas_limit": "4294967295",
  "gas_target_percentage": -100.0,
  "gas_used": "0",
  "gas_used_percentage": 0.0,
  "hash": "0xfe229c3c9869b286d63b1651bbc20da499c4f67d3a0924a61ab63f4e482c1326",
  "height": 3141995,
  "internal_transactions_count": 0,
  "is_pending_update": false,
  "miner": {
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
  "nonce": "0x0000000000000000",
  "parent_hash": "0xb9e3ee52488f7fcebae30e4ce3e9f12338e8bcb2e7b2f778ae36e93aeff8fe46",
  "priority_fee": "0",
  "rewards": [],
  "size": 619,
  "timestamp": "2026-11-14T08:51:16.000000Z",
  "total_difficulty": null,
  "transaction_fees": "0",
  "transactions_count": 0,
  "type": "block",
  "uncles_hashes": [],
  "withdrawals_count": 0
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
