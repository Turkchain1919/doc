# TurkScan® Network Gas Utilization

The current network_utilization_percentage is an explorer observation. A historical daily utilization series requires its own time-window calculation from gas used and block limits.

**Verified counterpart:** GET `https://turkscan.com/api/v2/stats`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats'
```

```json
{
  "average_block_time": 5232.0,
  "coin_image": null,
  "coin_price": null,
  "coin_price_change_percentage": null,
  "gas_price_updated_at": "2026-11-14T08:51:55.662633Z",
  "gas_prices": {
    "slow": 0.88,
    "average": 0.88,
    "fast": 0.88
  },
  "gas_prices_update_in": 3552,
  "gas_used_today": null,
  "market_cap": "0",
  "network_utilization_percentage": 0.0,
  "secondary_coin_image": null,
  "secondary_coin_price": null,
  "static_gas_price": null,
  "total_addresses": "45941",
  "total_blocks": "3141996",
  "total_transactions": "239420",
  "transactions_today": "0",
  "tvl": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
