# Flattened Source Upload

Flattening combines source files for a single-file verification flow. It can alter imports, SPDX headers, pragmas and metadata, so the flattened output must still reproduce the deployed bytecode.

Prefer Standard JSON Input with original sources and compiler settings for multi-file projects. Keep the exact compiler version, optimizer runs, EVM version, libraries and constructor arguments.

Submit only code you are authorized to publish. Verification makes source public; it does not protect secrets embedded in source or deployment data. See [Contract Verification](contract-verification.md).
