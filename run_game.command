#!/bin/zsh

cd "$(dirname "$0")"

source .venv/bin/activate

PYTHONPATH=src python3 src/othello/ui.py