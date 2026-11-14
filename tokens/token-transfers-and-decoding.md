# Token Transfers and Decoding

Token-transfer views are derived from recognized contract events. One transaction can emit multiple transfers, and one ERC-1155 batch can describe several token IDs.

Confirm the emitting contract address, amount or token ID, sender, recipient and parent transaction status. A token with a familiar symbol can be unrelated to an official asset.

Use integer base units and the actual token decimals for fungible tokens. See [Tokens API](../api-documentation/tokens-api.md) and [Logs](../transactions/event-logs.md).
