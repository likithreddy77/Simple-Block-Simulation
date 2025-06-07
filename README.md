# Basic Blockchain Simulation in Python

This is a simple simulation of a blockchain implemented in Python to demonstrate how blockchains maintain integrity and detect tampering.

## Objective

To help beginners understand the structure of a blockchain by:

- Creating a chain of 3 blocks
- Linking them using hashes
- Showing how tampering with one block affects the entire chain

##  Project Features

- Block structure with:
  - `index`
  - `timestamp`
  - `data`
  - `previous_hash`
  - `hash`
  - `nonce`
- SHA-256 hash function for block integrity
- Tampering challenge to observe hash invalidation
- Optional integrity checker to validate the chain
