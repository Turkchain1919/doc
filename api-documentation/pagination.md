# Pagination

V2 list endpoints commonly return `items` plus `next_page_params`. Pass the returned cursor fields back to the same endpoint, preserving the original filter. Stop when the cursor is null. Cursor fields vary by resource; do not invent a shared `page` or `offset` scheme for V2.

```javascript
const base = 'https://turkscan.com/api/v2/blocks';
let cursor = {};
for (;;) {
  const response = await fetch(`${base}?${new URLSearchParams(cursor)}`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const result = await response.json();
  for (const block of result.items) console.log(block.height, block.hash);
  if (!result.next_page_params) break;
  cursor = result.next_page_params;
}
```

Apply timeouts and a maximum page budget in production jobs. Data can change while paging; deduplicate identifiers and checkpoint processed results. Compatibility API pagination is action-specific and is documented separately.
