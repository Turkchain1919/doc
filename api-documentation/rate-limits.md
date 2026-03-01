---
description: '# Rate Limits'
---

# Rate Limits

Rate limits are applied per API key.

### Default Limits

```
• 5 requests per second (free tier)
• Higher tiers available for enterprise users
```

### Exceeded Limit Response

```
// Some code
{
  "status": "0",
  "message": "NOTOK",
  "result": "Max rate limit reached"
}
```

