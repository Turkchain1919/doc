---
icon: globe-pointer
---

# Network Info (RPC, Chain ID)

This section provides the essential network configuration details required to connect wallets, applications, and development tools to the Turkchain 1919 blockchain.

Turkchain 1919 operates as a **single-network blockchain**, and all interactions occur on the same unified network.

***

### 🌐 Network Details

| Parameter      | Value                                |
| -------------- | ------------------------------------ |
| Network Name   | Turkchain 1919                       |
| Chain ID       | `1919`                               |
| RPC Endpoint   | `https://rpc.turkchain1919.com`      |
| Block Explorer | `https://explorer.turkchain1919.com` |

These values are required when configuring wallets, deploying smart contracts, or interacting with the network programmatically.

***

### 🔌 RPC Endpoint

The RPC endpoint is the primary interface for communicating with the Turkchain 1919 network.

**RPC URL:**

```
https://rpc.turkchain1919.com
```

Through this endpoint, users and developers can:

* Query blockchain state
* Send signed transactions
* Interact with smart contracts
* Retrieve block and transaction data

The endpoint supports standard **EVM-compatible JSON-RPC methods**.

***

### 🆔 Chain ID

The Chain ID uniquely identifies the Turkchain 1919 network.

**Chain ID:** `1919`

This value is used to:

* Prevent cross-network replay attacks
* Ensure correct transaction signing
* Distinguish Turkchain 1919 from other EVM networks

Always verify the Chain ID before submitting transactions.

***

### 🦊 Wallet Configuration

To connect a wallet (such as MetaMask or compatible EVM wallets), use the following parameters:

* **Network Name:** Turkchain 1919
* **RPC URL:** `https://rpc.turkchain1919.com`
* **Chain ID:** `1919`
* **Currency Symbol:** (optional, network-defined)
* **Block Explorer URL:** `https://explorer.turkchain1919.com`

Once added, users can send transactions, interact with smart contracts, and view activity directly in the explorer.

***

### ⚠️ Network Scope

Turkchain 1919 currently operates **only one network**.

* There is no separate testnet or alternative environment
* Any future network changes will be announced explicitly
* Always rely on official documentation for updates

***

### 🔗 Related Sections

* **Explorer Overview** – How to navigate the explorer
* **Using the Explorer** – Search, blocks, transactions
* **For Developers** – RPC usage and API references

***

### ✅ Summary

* Turkchain 1919 is a single-network blockchain
* Chain ID and RPC configuration are fixed
* Explorer provides full transparency
* Standard EVM tooling is supported
