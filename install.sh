#!/bin/bash
# CryptXT - Installation Script
# For Linux and macOS

echo "CryptXT Installation Starting..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found!"
    echo "Please install Python 3.7 or higher: https://www.python.org/downloads/"
    exit 1
fi

echo "OK: Python found: $(python3 --version)"
echo ""

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 not found!"
    echo "Please install pip"
    exit 1
fi

echo "OK: pip found"
echo ""

# Install required packages
echo "Installing required packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "SUCCESS: Installation completed successfully!"
    echo ""
    echo "To start the application:"
    echo "   python3 cryptxt.py"
    echo ""
    echo "or"
    echo ""
    echo "   chmod +x cryptxt.py"
    echo "   ./cryptxt.py"
    echo ""
else
    echo ""
    echo "ERROR: Installation failed!"
    exit 1
fi
