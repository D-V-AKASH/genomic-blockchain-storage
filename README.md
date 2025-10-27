GENOMIC BLOCKCHAIN STORAGE

Live Demo:
https://genomic-data-backend.vercel.app/

A decentralized system for securely storing and managing genomic data using blockchain and IPFS.
It combines encryption, decentralized storage, and smart contracts to ensure privacy and controlled access.

Features:
Encrypts genomic data before upload
Stores encrypted files on IPFS (via Pinata/NFT.Storage)
Manages access using Ethereum smart contracts
React-based frontend for easy interaction

Tech Stack:
Backend: Python, Solidity
Frontend: React.js, Web3.js
Storage: IPFS (Pinata / NFT.Storage)
Blockchain: Ethereum

Quick Start:
# Clone the repo
git clone https://github.com/D-V-AKASH/genomic-blockchain-storage.git
cd genomic-blockchain-storage

# Backend setup
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate (Windows)

# Frontend setup
cd genomic-data-access
npm install
npm start

How It Works:
Encrypts genomic data locally
Uploads encrypted data to IPFS
Stores CID on blockchain
Grants/revokes access via smart contract

Author
D.V. AKASH
