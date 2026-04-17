# CryptXT

**Advanced File and Message Encryption Tool**

Military-grade encryption with AES-256-GCM, Argon2id key derivation, and HMAC integrity verification. A modern, secure, and user-friendly terminal application for protecting your sensitive data.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security: Military Grade](https://img.shields.io/badge/security-military%20grade-green.svg)]()
[![GitHub](https://img.shields.io/badge/github-CryptXT-blue.svg)](https://github.com/vyofgod/CryptXT)

## Features

### Advanced Security
- **AES-256-GCM**: Authenticated encryption with built-in integrity verification
- **Argon2id**: Memory-hard key derivation (winner of Password Hashing Competition)
- **HMAC-SHA256**: Additional integrity verification layer
- **Secure Random**: Cryptographically secure salt and nonce generation
- **Anti-Tampering**: Authentication tags prevent data modification

### Modern Interface
- Beautiful terminal UI with Rich library
- Real-time progress indicators
- Color-coded feedback (green for success, red for errors)
- Clean and intuitive menu system
- Spinner animations for visual feedback

### Cross-Platform
- Linux
- macOS
- Windows

### Functionality
- **Message Encryption**: Encrypt text messages to Base64 format
- **Message Decryption**: Decrypt Base64 encrypted messages
- **File Encryption**: Encrypt any file type with `.cryptxt` extension
- **File Decryption**: Restore encrypted files to original format
- **Security Info**: View detailed security specifications

## Installation

### Quick Install (All Systems)

#### Linux / macOS

```bash
# Clone the repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
chmod +x install.sh
./install.sh

# Start the application
python3 cryptxt.py
```

#### Windows (Command Prompt)

```cmd
REM Clone the repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

REM Run installation script
install.bat

REM Start the application
python cryptxt.py
```

#### Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
.\install.bat

# Start the application
python cryptxt.py
```

### Manual Installation

#### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- git

#### Step 1: Clone Repository

```bash
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT
```

#### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install cryptography argon2-cffi rich
```

#### Step 3: Run Application

**Linux/macOS:**
```bash
python3 cryptxt.py
```

**Windows:**
```cmd
python cryptxt.py
```

### Alternative: Direct Download

If you don't have git installed:

1. Download ZIP: [https://github.com/vyofgod/CryptXT/archive/refs/heads/main.zip](https://github.com/vyofgod/CryptXT/archive/refs/heads/main.zip)
2. Extract the archive
3. Open terminal/command prompt in the extracted folder
4. Run installation script or install dependencies manually

## Security Specifications

### Encryption Algorithm
- **Algorithm**: AES-256-GCM (Advanced Encryption Standard)
- **Key Size**: 256 bits
- **Mode**: Galois/Counter Mode with authentication
- **Nonce**: 12 bytes (96 bits) - unique per encryption
- **Tag**: 16 bytes (128 bits) - authentication tag

### Key Derivation Function

**Primary (Recommended): Argon2id**
- Time cost: 3 iterations
- Memory cost: 64 MB
- Parallelism: 4 threads
- Type: Hybrid (Argon2id)
- Resistant to: GPU attacks, side-channel attacks, time-memory trade-offs

**Fallback: PBKDF2-HMAC-SHA256**
- Iterations: 600,000 (OWASP 2024 recommendation)
- Used when Argon2 is not available

### Additional Security Layers
- **HMAC-SHA256**: 32-byte integrity verification
- **Salt**: 32 bytes of cryptographically secure random data
- **Secure Random**: Uses `secrets` module for all random generation

### Data Format

**Encrypted Data Structure:**
```
[SALT: 32 bytes] + [NONCE: 12 bytes] + [HMAC: 32 bytes] + [CIPHERTEXT + AUTH_TAG]
```

## Usage

### Encrypt a Message

1. Run the application: `python3 cryptxt.py`
2. Select option **1** (Encrypt Message)
3. Enter your message
4. Enter a strong password
5. Copy the encrypted Base64 output

**Example:**
```
Message: "Hello, World!"
Password: MySecurePass123!
Output: gAAAAABm... (Base64 encrypted string)
```

### Decrypt a Message

1. Select option **2** (Decrypt Message)
2. Paste the encrypted Base64 string
3. Enter the same password used for encryption
4. View the original message

### Encrypt a File

1. Select option **3** (Encrypt File)
2. Enter the file path (e.g., `document.pdf`)
3. Enter a strong password
4. File is saved with `.cryptxt` extension (e.g., `document.pdf.cryptxt`)

**Supported File Types:**
- Documents: `.pdf`, `.docx`, `.txt`, `.md`
- Images: `.jpg`, `.png`, `.gif`, `.bmp`
- Videos: `.mp4`, `.avi`, `.mkv`
- Archives: `.zip`, `.rar`, `.7z`
- Any other file type

### Decrypt a File

1. Select option **4** (Decrypt File)
2. Enter the encrypted file path (e.g., `document.pdf.cryptxt`)
3. Enter the password used for encryption
4. Original file is restored (e.g., `document.pdf`)

### View Security Information

Select option **5** to view detailed security specifications including:
- Encryption algorithm details
- Key derivation parameters
- Security level assessment

## Password Best Practices

### Strong Password Examples
- `MyS3cur3P@ssw0rd!2024`
- `Tr0pic@l_Sunset#99`
- `C0ffee&Code!Secure`

### Weak Password Examples
- `123456`
- `password`
- `qwerty`

### Password Guidelines
- Minimum 12 characters
- Mix of uppercase and lowercase letters
- Include numbers
- Include special characters (@, #, !, $, etc.)
- Avoid personal information
- Use a password manager

## Security Comparison

| Feature | CryptXT | Standard Tools |
|---------|---------|----------------|
| Encryption | AES-256-GCM | AES-256-CBC |
| Authentication | Built-in + HMAC | Manual |
| Key Derivation | Argon2id | PBKDF2 |
| GPU Resistance | High | Low |
| Memory-Hard | Yes | No |
| Tampering Detection | Automatic | Manual |

## Important Notes

### Password Recovery
- **Passwords cannot be recovered** - encryption is irreversible without the correct password
- Store passwords securely (use a password manager)
- Test decryption before deleting original files

### Backup Recommendations
- Always backup important files before encryption
- Test the decryption process with a copy first
- Store encrypted files and passwords separately

### Security Considerations
- This tool provides military-grade encryption
- Suitable for highly sensitive data
- No backdoors or password recovery mechanisms
- Open source - code can be audited

## Performance

| Operation | Small (<1MB) | Medium (1-10MB) | Large (>10MB) |
|-----------|--------------|-----------------|---------------|
| Message Encryption | ~0.5s | N/A | N/A |
| File Encryption | ~1s | ~2-5s | ~5-15s |
| File Decryption | ~1s | ~2-5s | ~5-15s |

*Performance varies based on hardware and Argon2 memory cost*

## Testing

### Linux / macOS

Create a test file:
```bash
echo "This is a test file for CryptXT encryption." > test.txt
```

Encrypt it:
```bash
python3 cryptxt.py
# Select option 3
# File: test.txt
# Password: TestPass123!
```

Verify encryption:
```bash
cat test.txt.cryptxt  # Should show encrypted binary data
```

Decrypt it:
```bash
python3 cryptxt.py
# Select option 4
# File: test.txt.cryptxt
# Password: TestPass123!
```

Verify decryption:
```bash
cat test.txt  # Should show original content
```

### Windows (Command Prompt)

Create a test file:
```cmd
echo This is a test file for CryptXT encryption. > test.txt
```

Encrypt it:
```cmd
python cryptxt.py
REM Select option 3
REM File: test.txt
REM Password: TestPass123!
```

Verify encryption:
```cmd
type test.txt.cryptxt
```

Decrypt it:
```cmd
python cryptxt.py
REM Select option 4
REM File: test.txt.cryptxt
REM Password: TestPass123!
```

Verify decryption:
```cmd
type test.txt
```

### Using Example File

The repository includes an `example.txt` file for testing:

```bash
# Linux/macOS
python3 cryptxt.py

# Windows
python cryptxt.py

# Then select option 3 and use: example.txt
```

## System Requirements

### Minimum Requirements
- **OS**: Linux, macOS, Windows 10/11
- **Python**: 3.7 or higher
- **RAM**: 128 MB (256 MB recommended for Argon2)
- **Disk**: 50 MB free space

### Tested On
- Ubuntu 20.04+, Fedora 35+, Debian 11+
- macOS 10.14+
- Windows 10, Windows 11

## Troubleshooting

### Common Issues

**Issue: "Python not found"**
```bash
# Linux (Debian/Ubuntu)
sudo apt install python3 python3-pip

# Linux (Fedora)
sudo dnf install python3 python3-pip

# macOS
brew install python3

# Windows: Download from https://www.python.org/downloads/
```

**Issue: "pip not found"**
```bash
# Linux
sudo apt install python3-pip  # Debian/Ubuntu
sudo dnf install python3-pip  # Fedora

# macOS
python3 -m ensurepip --upgrade

# Windows
python -m ensurepip --upgrade
```

**Issue: "Permission denied" (Linux/macOS)**
```bash
chmod +x cryptxt.py install.sh
```

**Issue: "Module not found"**
```bash
pip install --upgrade -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

**Linux/macOS:**
```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/CryptXT.git
cd CryptXT

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make changes and test
python3 cryptxt.py
```

**Windows:**
```cmd
REM Fork and clone
git clone https://github.com/YOUR_USERNAME/CryptXT.git
cd CryptXT

REM Create virtual environment
python -m venv venv
venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Make changes and test
python cryptxt.py
```

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly on your platform
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided "as is" without warranty of any kind. While it uses military-grade encryption, the developers are not responsible for any data loss. Always maintain backups of important files.

## Resources

- [AES-GCM Specification](https://csrc.nist.gov/publications/detail/sp/800-38d/final)
- [Argon2 Documentation](https://github.com/P-H-C/phc-winner-argon2)
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Cryptography Library](https://cryptography.io/)

## Support

For issues, questions, or suggestions:
- **Issues**: [GitHub Issues](https://github.com/vyofgod/CryptXT/issues)
- **Discussions**: [GitHub Discussions](https://github.com/vyofgod/CryptXT/discussions)
- **Documentation**: Check this README and code comments
- **Security**: Review security specifications above

## Quick Command Reference

### Installation Commands

| System | Command |
|--------|---------|
| Linux/macOS | `git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && ./install.sh` |
| Windows | `git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && install.bat` |

### Running Commands

| System | Command |
|--------|---------|
| Linux/macOS | `python3 cryptxt.py` |
| Windows | `python cryptxt.py` |

### Update Commands

```bash
# Linux/macOS
cd CryptXT
git pull origin main
pip install --upgrade -r requirements.txt

# Windows
cd CryptXT
git pull origin main
pip install --upgrade -r requirements.txt
```

## Links

- **Repository**: [https://github.com/vyofgod/CryptXT](https://github.com/vyofgod/CryptXT)
- **Issues**: [https://github.com/vyofgod/CryptXT/issues](https://github.com/vyofgod/CryptXT/issues)
- **Releases**: [https://github.com/vyofgod/CryptXT/releases](https://github.com/vyofgod/CryptXT/releases)

---

**Stay secure! Protect your data with CryptXT.**

*Version 1.0.0* | [GitHub](https://github.com/vyofgod/CryptXT)
