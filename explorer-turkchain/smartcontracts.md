---
icon: globe-pointer
---

# Smart Contracts

A smart contract is a program deployed on the TurkChain blockchain.\
When you interact with a smart contract, you either:

* **Read data** from the blockchain (for example, checking balances or configuration values), or
* **Write data** by submitting a transaction (for example, transferring tokens or approving permissions).

Some interactions are **read-only** and safe.\
Others **change blockchain state** and require signing a transaction with your wallet.

On **TurkChain Explorer**, you can interact directly with smart contracts using the **Read Contract** and **Write Contract** tabs on a contract’s page. This allows you to inspect and interact with contracts even when no custom user interface is available.

***

### Read Contract vs Write Contract

#### Read Contract

* Fetches public data exposed by the contract
* Does **not** change blockchain state
* Does **not** require gas
* Does **not** require a wallet signature

Read calls are safe and useful for inspecting balances, configuration values, or contract metadata.

***

#### Write Contract

* Submits a transaction that changes blockchain state
* Requires a connected wallet
* Requires paying **TURK gas**
* Actions are usually **irreversible**

Examples include:

* Transferring tokens
* Approving token allowances
* Calling administrative or permissioned functions

⚠️ **Always review write actions carefully before signing.**

***

### How Contract Interactions Work on TurkChain Explorer

When you use the **Read** or **Write Contract** tabs:

* The request runs **locally in your browser**
* Data is fetched directly from a **TurkChain RPC node**
* Requests do **not** pass through TurkChain Explorer servers

For read-only calls, the explorer uses a default public RPC.\
For write calls, your wallet submits the transaction directly to the network.

This design improves transparency and reduces trust assumptions.

***

### The “Verified” Contract Checkmark

Verified smart contracts on TurkChain Explorer display a **green checkmark ✅** on the **Contract** tab.

This means:

* The contract’s source code is **public**
* The source code **matches the deployed bytecode** on TurkChain

⚠️ **Important:**\
“Verified” does **not** mean:

* The contract is safe
* The contract is audited
* The contract is free of vulnerabilities

It only confirms that the published code matches what is running onchain.

If a contract is **not verified**, you cannot see what it will do when you sign a transaction.\
Avoid interacting with unverified contracts unless you fully trust the source.

***

### Reviewing Contract Code Before Interaction

Before signing any transaction:

* Read the function name and parameters carefully
* Understand what the function does
* Confirm which assets are affected

You may use:

* Your own code review
* Automated code analysis tools
* AI-based code explanation tools

If you do not understand the function, **do not sign the transaction**.

***

### Public Name Tags

Some contracts display a **public name tag** on TurkChain Explorer.

A name tag:

* Identifies the project or protocol
* Often links to an official website or documentation

If a contract has **no name tag**, always verify the contract address through:

* Official project websites
* Trusted announcements
* Verified social channels

Never rely on name similarity alone.

***

### Additional Security Insights

TurkChain Explorer may display **additional information cards** provided by trusted third parties.

These can include:

* Scam warnings
* Token behavior flags
* Audit references
* Risk or vulnerability indicators

Such signals are meant to **assist decision-making**, not replace your own judgment.

***

### Token Reputation Awareness

Not all tokens are equally safe.

When interacting with token contracts, pay attention to:

* Token reputation indicators
* Warning labels or risk flags

If a token is marked as:

* Suspicious
* Unsafe
* Spam

⚠️ Proceed with extreme caution or avoid interaction entirely.

***

### Limit Token Approvals

When approving tokens for a smart contract:

* Approve **only the amount you intend to use**
* Avoid unlimited approvals unless necessary

If you approve more than required, the contract may later spend the remaining allowance **without additional confirmation**.

Regularly review and revoke unused approvals to reduce risk.

***

### Review Wallet Transaction Simulations

Modern wallets often display a **transaction simulation** before you confirm.

Always check:

* Which tokens are leaving your wallet
* Which addresses receive them
* Whether permissions or approvals are being granted

If anything looks unexpected, **reject the transaction immediately**.

***

### Final Reminder

TurkChain Explorer helps you **inspect and interact** with onchain data, but:

* It does **not** audit contracts
* It does **not** guarantee contract safety
* You are responsible for **every transaction you sign**

If something feels unclear, rushed, or confusing, it is usually safer to **pause, verify, and review** before proceeding.
