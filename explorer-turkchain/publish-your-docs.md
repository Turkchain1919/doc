---
icon: globe-pointer
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/yE16Xb3IemPxJWydtPOj/getting-started/publish-your-docs
---

# Using the Explorer

The Turkchain 1919 Explorer provides a comprehensive interface to inspect all on-chain activity in real time.\
It allows users to search, verify, and analyze data directly from the blockchain without relying on third-party services.

This section explains how to use the explorer to search for data, understand blocks, and inspect transactions.

***

### 🔎 Search Functionality

The search bar is the primary entry point for navigating the Turkchain 1919 blockchain.

Using the search bar, you can look up:

* Transaction hashes
* Wallet addresses
* Block numbers or block hashes
* Token contract addresses
* Smart contract addresses

Simply paste the relevant value into the search field and press **Enter**.

#### Supported Search Types

| Input Type       | Example  |
| ---------------- | -------- |
| Transaction Hash | `0x...`  |
| Wallet Address   | `0x...`  |
| Block Number     | `123456` |
| Block Hash       | `0x...`  |
| Contract Address | `0x...`  |

The explorer automatically detects the input type and redirects you to the appropriate page.

***

### 🧱 Blocks

Blocks are the fundamental units of the Turkchain 1919 blockchain.\
Each block contains a set of validated transactions and metadata describing the state of the network at a specific point in time.

#### Block Information

When viewing a block, you can inspect:

* **Block Number** – The sequential height of the block
* **Block Hash** – Unique identifier of the block
* **Timestamp** – When the block was produced
* **Transactions Count** – Number of transactions included
* **Gas Used / Gas Limit** – Execution metrics
* **Validator / Producer** – Entity that proposed the block

Blocks are produced continuously, ensuring fast confirmation times and network finality.

#### Navigating Blocks

* Use **Next / Previous** buttons to move between blocks
* Click a block number to view full block details
* Click individual transactions to inspect execution details

This allows users to trace activity chronologically across the chain.

***

### 🔄 Transactions

Transactions represent state changes on the blockchain.\
They may include token transfers, smart contract interactions, or contract deployments.

#### Transaction Overview

Each transaction page displays detailed execution data, including:

* **Transaction Hash** – Unique identifier
* **Status** – Success or failure
* **Block Number** – Block where the transaction was included
* **Timestamp** – Execution time
* **From / To** – Sender and recipient addresses
* **Value** – Amount transferred (if applicable)
* **Gas Limit / Gas Used** – Execution cost
* **Transaction Fee** – Total fee paid

#### Transaction Types

Turkchain 1919 supports multiple transaction types:

* Native token transfers
* ERC-20 compatible token transfers
* Smart contract calls
* Smart contract deployments

Each type can be identified by inspecting the transaction input data and logs.

***

### 📜 Logs & Events

For transactions interacting with smart contracts, the explorer provides access to:

* Event logs
* Indexed parameters
* Emitted contract events

These logs are essential for developers tracking contract behavior, token transfers, and protocol activity.

***

### 🧭 Tracing & Transparency

The explorer ensures full transparency by allowing users to:

* Trace transactions back to their originating block
* Inspect historical activity of any address
* Verify execution outcomes independently

All data displayed in the explorer is sourced directly from the Turkchain 1919 blockchain.

***

### 👥 Who Is This For?

The explorer is designed for multiple user types:

* **Users** checking balances and transaction status
* **Token holders** tracking transfers and activity
* **Developers** debugging and verifying smart contracts
* **Projects** auditing on-chain behavior

***

### 📌 Best Practices

* Always verify transaction status before assuming completion
* Use block confirmations for high-value transfers
* Cross-check contract addresses before interacting

***

### 🔗 Related Sections

* **Addresses** – Wallet balances and activity
* **Tokens** – Token holders and transfers
* **Contracts** – Smart contract details and verification
* **Token Verification** – Publish token metadata
* **Contract Verification** – Verify smart contract source code
