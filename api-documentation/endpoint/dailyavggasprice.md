# TurkScan® Historical Gas Prices

A daily average requires a specified weighting policy and the actual effective gas prices of included transactions. Current gas estimates are not historical averages.

**Verified counterpart:** GET `https://turkscan.com/api/v2/transactions`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions'
```

```json
{
  "items": [
    {
      "has_error_in_internal_transactions": null,
      "block_number": 3117475,
      "exchange_rate": null,
      "transaction_types": [
        "contract_call"
      ],
      "historic_exchange_rate": null,
      "nonce": 2,
      "timestamp": "2026-11-12T21:19:21.000000Z",
      "base_fee_per_gas": "1000000000",
      "token_transfers": null,
      "fhe_operations_count": 0,
      "decoded_input": null,
      "gas_price": "1000100000",
      "gas_limit": "260611",
      "fee": {
        "type": "actual",
        "value": "175482546500000"
      },
      "method": "0x7c39d130",
      "authorization_list": [],
      "to": {
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
      "status": "ok",
      "gas_used": "175465",
      "from": {
        "ens_domain_name": null,
        "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
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
      "value": "0",
      "created_contract": null,
      "transaction_tag": null,
      "max_priority_fee_per_gas": "100000",
      "position": 0,
      "confirmations": 24533,
      "token_transfers_overflow": null,
      "type": 2,
      "transaction_burnt_fee": "175465000000000",
      "confirmation_duration": [
        0
      ],
      "revert_reason": null,
      "max_fee_per_gas": "2000100000",
      "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "result": "success",
      "is_pending_update": false,
      "raw_input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791c [excerpt]",
      "priority_fee": "17546500000"
    }
  ],
  "next_page_params": {
    "index": 0,
    "block_number": 2948806
  }
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
