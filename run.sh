#!/bin/bash
if [ ! -f "venv/bin/activate" ]; then
  ./install.sh
fi
source venv/bin/activate
python3 main.py
deactivate
