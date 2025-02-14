#!/bin/bash

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1
}

# Check for Python3, pip, and virtualenv
if ! check_command python3 || ! check_command pip || ! check_command virtualenv; then
    echo "⚠️ Error: Python3, pip, and virtualenv must be installed."
    echo "Install them using:"
    echo "  sudo apt install python3 python3-pip virtualenv   # Debian-based"
    echo "  sudo dnf install python3 python3-pip python3-virtualenv   # Fedora"
    echo "  sudo pacman -S python python-pip virtualenv   # Arch"

else
    # Create virtual environment
    virtualenv venv

    # Install dependencies
    venv/bin/pip install -r requirements.txt

    echo "✅ Virtual environment setup complete and activated."
fi