# Token Development

Choose ERC-20, ERC-721 or ERC-1155 based on the asset model. Use maintained implementations, pin dependencies and test minting, transfers, approvals, burning, access controls and failure paths.

Specify decimals and supply rules explicitly for fungible tokens. For NFTs, document metadata mutability and storage availability. Avoid privileged behavior that is not clearly communicated to users.

After deployment, verify source and inspect emitted events on TurkScan®. Token listing, icon review and source verification are different steps. A wrapped asset additionally needs a documented backing and redemption mechanism.
