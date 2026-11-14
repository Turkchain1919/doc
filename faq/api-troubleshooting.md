# API Troubleshooting

Check HTTP status and response body. V2 validation errors differ from compatibility API status envelopes. Follow the returned cursor, use bounded backoff on 429/503 and preserve large integer strings. The bare `/api/v2` path is not an endpoint directory; use the documented resource paths.
