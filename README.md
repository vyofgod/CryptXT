# CryptXT

**Advanced File and Message Encryption Tool**

Military-grade encryption with AES-256-GCM, Argon2id key derivation, and HMAC integrity verification.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/cryptxt.svg)](https://badge.fury.io/py/cryptxt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/cryptxt)](https://pepy.tech/project/cryptxt)

## Features

- **AES-256-GCM**: Authenticated encryption with built-in integrity verification
- **Argon2id**: Memory-hard key derivation (resistant to GPU attacks)
- **HMAC-SHA256**: Additional integrity verification layer
- **Cross-Platform**: Linux, macOS, Windows
- **Modern UI**: Beautiful terminal interface with progress indicators

## Quick Install

```bash
pip install cryptxt
cryptxt
```

## Installation Methods

### Method 1: pip (Recommended)
```bash
pip install cryptxt
cryptxt
```

### Method 2: npx (No installation)
```bash
npx cryptxt
```

### Method 3: From Source
```bash
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT
pip install -r requirements.txt
python3 cryptxt.py
```

## Usage

### Encrypt a Message
1. Run `cryptxt`
2. Select option **1** (Encrypt Message)
3. Enter your message and password
4. Copy the encrypted Base64 output

### Decrypt a Message
1. Select option **2** (Decrypt Message)
2. Paste the encrypted Base64 string
3. Enter the password

### Encrypt a File
1. Select option **3** (Encrypt File)
2. Enter file path (e.g., `document.pdf`)
3. Enter password
4. File saved as `document.pdf.cryptxt`

### Decrypt a File
1. Select option **4** (Decrypt File)
2. Enter encrypted file path (e.g., `document.pdf.cryptxt`)
3. Enter password
4. Original file restored

## Security Specifications

### Encryption
- **Algorithm**: AES-256-GCM
- **Key Size**: 256 bits
- **Nonce**: 12 bytes (unique per encryption)
- **Auth Tag**: 16 bytes (prevents tampering)

### Key Derivation
- **Primary**: Argon2id (3 iterations, 64 MB memory, 4 threads)
- **Fallback**: PBKDF2-HMAC-SHA256 (600,000 iterations)

### Additional Security
- HMAC-SHA256 integrity verification
- 32-byte cryptographically secure salt
- Secure random generation using `secrets` module

## Password Best Practices

**Strong passwords:**
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, special characters
- Avoid personal information

**Examples:**
- Good: `MyS3cur3P@ssw0rd!2024`
- Bad: `password123`

## Important Notes

- **No password recovery** - Encryption is irreversible without the correct password
- **Backup files** before encryption
- **Test decryption** before deleting originals
- **Store passwords** securely (use a password manager)

## Testing

```bash
# Create test file
echo "Test message" > test.txt

# Encrypt
cryptxt
# Select 3, enter: test.txt, password: test123

# Decrypt
cryptxt
# Select 4, enter: test.txt.cryptxt, password: test123
```

## Links

- **PyPI**: https://pypi.org/project/cryptxt/
- **GitHub**: https://github.com/vyofgod/CryptXT
- **Issues**: https://github.com/vyofgod/CryptXT/issues
- **Documentation**: Full installation guide in [INSTALL.md](INSTALL.md)

## Contributing

Contributions welcome! Please submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided "as is" without warranty. While it uses military-grade encryption, always maintain backups of important files.

---

**Protect your data with CryptXT**

*Version 1.0.1*
