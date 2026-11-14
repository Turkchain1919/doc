# Method Identifiers and Decoded Input

A typical ABI call begins with a four-byte function selector followed by arguments. TurkScan attempts to decode using available ABI and signature data. Selectors can collide and custom fallback logic can behave differently.

## What to check

Compare the called address and implementation with the intended method. Preserve raw input when decoding is unavailable. Treat a friendly method label as an interpretation, not proof of contract behavior.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/transactions/input-data-and-decoding). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
