# Python AES Implementation

**Author:** Vladyslav Chornyi

## Overview
This repository contains a from-scratch Python implementation of the Advanced Encryption Standard (AES) algorithm. I originally developed this as my term project at the National Taras Shevchenko University of Kyiv. The goal was to build a rigorous, educational model of symmetric-key cryptography, block ciphers, and finite field arithmetic without relying on external cryptographic libraries.

## Features
* **Multiple Key Sizes:** Supports AES-128, AES-192, and AES-256 via dedicated classes.
* **Full Encryption/Decryption Pipeline:** Implements all core mathematical transformations (SubBytes, ShiftRows, MixColumns, AddRoundKey) and the AES key schedule.
* **Flexible Input Handling:** Automatically parses hex strings (with or without spaces) and raw byte lists.
* **Zero Dependencies:** Built entirely using standard Python to expose the internal mechanics of the cipher.

## Usage

The implementation provides three main classes based on your required key size: `AES_128`, `AES_192`, and `AES_256`. Both plaintext and keys can be passed directly as hex strings.

```python
from AES import AES_128, hexstr

# Initialize the AES-128 cipher
aes = AES_128()

# Define plaintext and key as hex strings
plaintext = "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34"
key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"

# Encrypt the plaintext (returns a list of bytes)
ciphertext_bytes = aes.encrypt(plaintext, key)
print(f"Ciphertext: {hexstr(ciphertext_bytes)}")

# Decrypt the ciphertext back to plaintext
decrypted_bytes = aes.decrypt(ciphertext_bytes, key)
print(f"Decrypted:  {hexstr(decrypted_bytes)}")
```

## Testing
The repository includes a `tests.py` suite that verifies the encryption and decryption logic against official AES standard test vectors. It also includes file-based performance benchmarking. You can run the test suite directly:

```bash
python tests.py
```

## Disclaimer
This implementation is intended strictly for educational and academic purposes to demonstrate cryptographic principles. It is not optimized for side-channel resistance or production security.
