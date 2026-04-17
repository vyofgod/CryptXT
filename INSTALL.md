# CryptXT Installation Guide

Complete installation instructions for all operating systems.

## Table of Contents
- [Linux](#linux)
- [macOS](#macos)
- [Windows](#windows)
- [Troubleshooting](#troubleshooting)

---

## Linux

### Ubuntu / Debian / Linux Mint

```bash
# Install Python and pip (if not already installed)
sudo apt update
sudo apt install python3 python3-pip git -y

# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
chmod +x install.sh
./install.sh

# Start application
python3 cryptxt.py
```

### Fedora / RHEL / CentOS

```bash
# Install Python and pip (if not already installed)
sudo dnf install python3 python3-pip git -y

# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
chmod +x install.sh
./install.sh

# Start application
python3 cryptxt.py
```

### Arch Linux / Manjaro

```bash
# Install Python and pip (if not already installed)
sudo pacman -S python python-pip git

# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
chmod +x install.sh
./install.sh

# Start application
python3 cryptxt.py
```

### Manual Installation (All Linux)

```bash
# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x cryptxt.py

# Run
./cryptxt.py
```

---

## macOS

### Using Homebrew (Recommended)

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and git
brew install python3 git

# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
chmod +x install.sh
./install.sh

# Start application
python3 cryptxt.py
```

### Using System Python

```bash
# Clone repository
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x cryptxt.py

# Run
python3 cryptxt.py
```

---

## Windows

### Windows 10 / 11 (Command Prompt)

```cmd
REM Install Python from https://www.python.org/downloads/
REM Make sure to check "Add Python to PATH" during installation

REM Install Git from https://git-scm.com/download/win

REM Open Command Prompt and run:
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

REM Run installation script
install.bat

REM Start application
python cryptxt.py
```

### Windows PowerShell

```powershell
# Install Python from https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation

# Install Git from https://git-scm.com/download/win

# Open PowerShell and run:
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT

# Run installation script
.\install.bat

# Start application
python cryptxt.py
```

### Windows (Manual Installation)

1. **Install Python**
   - Download from: https://www.python.org/downloads/
   - Run installer
   - Check "Add Python to PATH"
   - Click "Install Now"

2. **Install Git**
   - Download from: https://git-scm.com/download/win
   - Run installer with default settings

3. **Clone and Install**
   ```cmd
   git clone https://github.com/vyofgod/CryptXT.git
   cd CryptXT
   pip install -r requirements.txt
   python cryptxt.py
   ```

### Windows (Without Git)

1. Download ZIP: https://github.com/vyofgod/CryptXT/archive/refs/heads/main.zip
2. Extract to a folder
3. Open Command Prompt in that folder
4. Run:
   ```cmd
   pip install -r requirements.txt
   python cryptxt.py
   ```

---

## Troubleshooting

### Python Not Found

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

**macOS:**
```bash
brew install python3
```

**Windows:**
- Download and install from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH"

### pip Not Found

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install python3-pip

# Fedora
sudo dnf install python3-pip

# Arch
sudo pacman -S python-pip
```

**macOS:**
```bash
python3 -m ensurepip --upgrade
```

**Windows:**
```cmd
python -m ensurepip --upgrade
```

### Git Not Found

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

**macOS:**
```bash
brew install git
```

**Windows:**
- Download from: https://git-scm.com/download/win

### Permission Denied (Linux/macOS)

```bash
chmod +x cryptxt.py install.sh
```

### Module Not Found Error

```bash
# Linux/macOS
pip3 install --upgrade -r requirements.txt

# Windows
pip install --upgrade -r requirements.txt
```

### Argon2 Installation Issues

If argon2-cffi fails to install:

**Linux:**
```bash
# Install build tools first
sudo apt install build-essential python3-dev  # Ubuntu/Debian
sudo dnf install gcc python3-devel            # Fedora
sudo pacman -S base-devel                     # Arch

# Then install
pip3 install argon2-cffi
```

**macOS:**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Then install
pip3 install argon2-cffi
```

**Windows:**
- Install Visual C++ Build Tools from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Then run: `pip install argon2-cffi`

Note: CryptXT will work without argon2-cffi, but will use PBKDF2 instead (less secure).

---

## Verification

After installation, verify it works:

**Linux/macOS:**
```bash
python3 cryptxt.py
# You should see the CryptXT banner and menu
```

**Windows:**
```cmd
python cryptxt.py
REM You should see the CryptXT banner and menu
```

---

## Updating

To update to the latest version:

```bash
# Navigate to CryptXT directory
cd CryptXT

# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Run
python3 cryptxt.py  # Linux/macOS
python cryptxt.py   # Windows
```

---

## Uninstallation

To remove CryptXT:

**Linux/macOS:**
```bash
# Remove directory
rm -rf CryptXT

# Optionally remove Python packages
pip3 uninstall cryptography argon2-cffi rich
```

**Windows:**
```cmd
REM Remove directory
rmdir /s CryptXT

REM Optionally remove Python packages
pip uninstall cryptography argon2-cffi rich
```

---

## Quick Reference

| System | Install Command |
|--------|----------------|
| Ubuntu/Debian | `sudo apt install python3 python3-pip git && git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && ./install.sh` |
| Fedora | `sudo dnf install python3 python3-pip git && git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && ./install.sh` |
| Arch | `sudo pacman -S python python-pip git && git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && ./install.sh` |
| macOS | `brew install python3 git && git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && ./install.sh` |
| Windows | `git clone https://github.com/vyofgod/CryptXT.git && cd CryptXT && install.bat` |

---

**Need help?** Open an issue: https://github.com/vyofgod/CryptXT/issues
