#!/bin/bash
FILENAME="sample.txt"

if [[ -f "$FILENAME" ]]; then
    python3 main.py "$FILENAME"
else
    touch "$FILENAME"
    python3 main.py "$FILENAME"
fi
