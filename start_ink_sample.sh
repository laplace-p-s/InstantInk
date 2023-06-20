#!/bin/bash
FILENAME="sample.txt"

if [[ -f "$FILENAME" ]]; then
    python main.py "$FILENAME"
else
    touch "$FILENAME"
    python main.py "$FILENAME"
fi
