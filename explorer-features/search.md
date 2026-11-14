# Search

Search accepts complete address and transaction identifiers, block numbers and indexed token names or symbols. Exact identifiers are safer than ambiguous names.

Token search can return multiple contracts with the same ticker. Confirm chain, contract address and metadata before opening a wallet interaction. Search indexing may lag current RPC state.

API clients can use `GET /api/v2/search?q=TURK`, quick search and redirect checks. See [Search API](../api-documentation/search-api.md).
