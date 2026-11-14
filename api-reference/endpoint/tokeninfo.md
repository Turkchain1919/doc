# TurkScan® Token Metadata

Metadata can include name, symbol, decimals, standard and supply. Operator badges and icons are separate review signals; null prices remain unavailable.

**Verified counterpart:** GET `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

```json
{
  "address_hash": "0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271",
  "circulating_market_cap": null,
  "circulating_supply": null,
  "decimals": "18",
  "exchange_rate": null,
  "holders_count": "6",
  "icon_url": null,
  "name": "777",
  "new_ui_multiplier": null,
  "reputation": "ok",
  "symbol": "7777",
  "total_supply": "1000000000000000000000000",
  "type": "ERC-20",
  "ui_multiplier": null,
  "ui_multiplier_effective_at": null,
  "volume_24h": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
