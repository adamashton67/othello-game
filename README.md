# Othello Game

## Current Version

v1.0

This is a Python project of a playable version of the board game Othello.

The aim of the project was for me to practise building a structured software project using Python, Git, testing, and clear commits.

## Version 1 Features

The first playable version will be a local two-player game with:

- An 8x8 board
- Black and white pieces
- Click-to-place moves
- Valid move checking
- Automatic piece flipping
- Turn indicator
- Live black and white piece totals
- Game-over detection
- Winner display

## Potential Future Improvements

Possible future improvements include:

- Highlighting valid moves
- Restart button
- Main menu
- Simple AI opponent
- Difficulty levels
- Animations
- Sound effects

## Requirements

- Python 3.13
- Pygame 2.6.1

## Running the Game

### macOS

Double-click:

```text
run_game.command
```

Or run from Terminal:

```bash
source .venv/bin/activate
PYTHONPATH=src python3 src/othello/ui.py
```