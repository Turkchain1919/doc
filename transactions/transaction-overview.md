# Transaction Overview

A transaction is a signed instruction submitted to Turkchain® Mainnet. Its hash identifies it. Key fields include sender, recipient, nonce, value, input data, gas settings and, after inclusion, block and receipt status.

An outer transaction can deploy a contract, call a contract or transfer native TURK. One transaction may generate several token transfer events and internal calls. These are not separate signed transactions.

Use [Transaction Status](transaction-status.md), [Gas Mechanics](gas-mechanics.md) and [Event Logs](event-logs.md) to interpret the result.
