# Fritz Maze

A fun and challenging maze game built with Python and Pygame. Navigate through randomly generated mazes, beat the clock in Time Trial mode, and save your favorite mazes to challenge yourself later.

## Features

- **Random Maze Generation**: Every game is unique!
- **Difficulty Levels**: Choose between Easy, Medium, and Hard.
- **Time Trial Mode**: Race against the clock and set new records.
- **VS Mode (Coming soon!)**: Compete against an AI opponent! 
- **Save & Load**: Save generated mazes and reload them anytime.
- **Cross-Platform**: Works on both Windows and Linux.

## Prerequisites

- **Python**: Version 3.13 or higher is recommended.
  - On Windows, install with `winget install Python.Python.3.13` inside PowerShell.
- **uv**: A fast Python package manager.
  - On Windows, install with `winget install --id=astral-sh.uv  -e` inside PowerShell.

## Installation

- Install Prerequisite Tools:
  - To install Python, follow the [official instructions](https://www.python.org/downloads/).
  - To install UV, follow the [official instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
    - On Windows, [WinGet](https://winstall.app/apps/astral-sh.uv) is recommended.
- Download the zip file here on GitHub and extract it to a folder of your choice.

## How to Run

### Windows

1. Navigate to the project folder in Explorer.
2. Right-click in the explorer and select **Open In Terminal**.
3. Run the game by executing the following command:
   ```powershell
   uv run main.py
   ```

### Linux

1. Open your **Terminal**.
2. Navigate to the project folder.
3. Run the game with the following command:
   ```bash
   uv  run main.py
   ```

## Controls

- **Move**: Use **Arrow Keys** or **WASD**.
- **Select/Interact**: Use the **Mouse** to navigate menus and click buttons.
- **Scroll**: Use the **Mouse Wheel** to scroll through saved mazes in the Load Menu.

## How to Play

1. **Main Menu**: Choose "Time Trial" to start a new game or "Load Maze" to play a previously saved one.
2. **Select Difficulty**: Choose your preferred challenge level.
3. **Maze Generation**: Watch as the maze is built step-by-step.
4. **Race**: Once the player spawns (red circle), move towards the finish line (represented by the end of the path).
5. **Win**: Reach the exit to stop the timer and see if you set a new record!
6. **Save**: After finishing a maze, you can save it to play again later.

## License

This project is licensed under the MIT License - see the LICENSE file for details (if applicable).
