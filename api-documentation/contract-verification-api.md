# Contract Verification API

`GET https://turkscan.com/api/v2/smart-contracts/verification/config` returned 200. Its response lists compiler choices, EVM targets, license types and verifier flags. Read it immediately before choosing a verification method.

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/smart-contracts/verification/config'
```

The Rust verifier is enabled. The audit did not submit verification requests, publish source, deploy contracts or sign transactions. The following Solidity submission routes were confirmed in the deployed-version router/controller source, but a successful job is not claimed:

| Method | Endpoint | Required input |
| --- | --- | --- |
| POST | `https://turkscan.com/api/v2/smart-contracts/{address_hash}/verification/via/standard-input` | Path address, `compiler_version`, `files` containing compiler Standard JSON Input |
| POST | `https://turkscan.com/api/v2/smart-contracts/{address_hash}/verification/via/flattened-code` | Path address, `compiler_version`, `source_code` |
| POST | `https://turkscan.com/api/v2/smart-contracts/{address_hash}/verification/via/multi-part` | Path address, `compiler_version`, source `files` |

For standard input, send multipart form fields with `files[0]` as the JSON file. Optional fields include `contract_name`, `constructor_args`, `autodetect_constructor_args` and `license_type`. Flattened code additionally accepts `is_optimization_enabled`, `optimization_runs`, `evm_version` and `libraries`; multipart libraries are a JSON string. Values must match the original build, not a generic example.

```bash
# Deliberate publication action; replace values with your own exact build inputs.
curl 'https://turkscan.com/api/v2/smart-contracts/YOUR_CONTRACT_ADDRESS/verification/via/standard-input' \
  -F 'compiler_version=YOUR_EXACT_COMPILER_VERSION' \
  -F 'files[0]=@standard-input.json' \
  -F 'contract_name=YOUR_CONTRACT_NAME'
```

A controller acceptance response has a `message` indicating verification was started; it is asynchronous and does not establish a bytecode match. No successful response is fabricated here. Poll the [contract detail](smart-contracts-api.md) to check the published result. Invalid address, missing files, unsupported method, compiler failure, existing verification and bytecode mismatch must be handled as distinct outcomes.

Generic Vyper, Sourcify and chain-specific methods are not listed as enabled merely because their routes exist. See [Contract Verification](../smart-contracts/contract-verification.md).
