# TurkScan® Address Labels and Metadata

Inspect public address metadata returned by the deployment. A private user tag is different from public metadata; bulk third-party label databases are not implied.

**Verified counterpart:** GET `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

```json
{
  "block_number_balance_updated_at": 3117475,
  "coin_balance": "9999473528358100000",
  "creation_status": null,
  "creation_transaction_hash": null,
  "creator_address_hash": null,
  "ens_domain_name": null,
  "exchange_rate": null,
  "has_beacon_chain_withdrawals": false,
  "has_logs": false,
  "has_token_transfers": false,
  "has_tokens": false,
  "has_validated_blocks": false,
  "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
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
  "token": null,
  "watchlist_address_id": null,
  "watchlist_names": []
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
