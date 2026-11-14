# Architecture Overview

A wallet signs a transaction locally and submits it to a Turkchain® RPC node. The network executes and includes it in a block. TurkScan® indexes blocks, receipts, logs and available execution traces, then exposes the indexed data through its website and APIs.

TurkScan® uses Blockscout-based explorer infrastructure, with TurkScan branding and operator-managed features. The inspected backend reports version `12.0.1`; statistics and source verification use separate services. The explorer is a view of the network, not the network's consensus engine.

An RPC receipt may appear before the explorer finishes indexing it. A token list, badge or price is explorer metadata and does not change on-chain ownership. A source match proves a relationship between submitted source and deployed bytecode, not contract safety.

GitHub is the documentation source and the existing GitBook site is the publication platform. No documentation container or separate documentation server is required.
