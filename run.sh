#!/bin/bash
if [ ! -f "venv/bin/activate" ]; then
  python3 install.py
fi
source venv/bin/activate
python3 main.py
deactivate
