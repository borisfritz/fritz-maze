# Fritz Maze

A fun and challenging maze game built with Python and Pygame. Navigate through randomly generated mazes, beat the clock in Time Trial mode, and save your favorite mazes to challenge yourself later.

## Features

- **Random Maze Generation**: Every game is unique!
- **Difficulty Levels**: Choose between Easy, Medium, and Hard.
- **Time Trial Mode**: Race against the clock and set new records.
- **Versus Mode**: Compete against an AI opponent! 
- **Save & Load**: Save generated mazes and reload them anytime.
- **Cross-Platform**: Works on both Windows and Linux.

## Prerequisites

- **Python**: Version 3.13 
- **uv**: A fast Python package manager

## Installation and Usage

### Windows
- Right-click the Start button and open **Terminal**
  - Install uv via the terminal with [WinGet](https://docs.astral.sh/uv/getting-started/installation/#winget) command: `winget install -e --id astral-sh.uv`
  - Install Python 3.13 with the [uv](https://docs.astral.sh/uv/guides/install-python/#installing-a-specific-version) command `uv python install Python3.13` inside the terminal.
    - Pygame doesn't seem to run with Python 3.14 on windows. Feel free to solve that problem yourself!  I'm moving on with my boot.dev courses. =D
- Download the zip file here on GitHub and extract it to a folder of your choice.
- Navigate to the project folder in your terminal and run the command `uv sync` to install all dependencies.
    - This can be easily done by right-clicking the project folder and selecting **Open In Terminal**.
- Run the game with `uv run main.py` while in the project folder.
  - Enjoy!

### Linux
- Install uv and Python via the terminal with your appropriate package manager.
- Download the zip file here on GitHub and extract it to a folder of your choice.
- Navigate to the project folder in your terminal and run the command `uv sync` to install all dependencies.
- Run the game with `uv run main.py` while in the project folder.
  - Enjoy!

## Controls

- **Move**: Use **Arrow Keys** or **WASD**.
- **Select/Interact**: Use the **Mouse** to navigate menus and click buttons.
- **Scroll**: Use the **Mouse Wheel** to scroll through saved mazes in the Load Menu.

## How to Play

1. **Main Menu**: Choose "Time Trial" or "Versus" to start a new game or "Load Maze" to play a previously saved Time Trial Maze.
2. **Select Difficulty**: Choose your preferred challenge level.
3. **Maze Generation**: Watch as the maze is built step-by-step.
4. **Race**: Once the player spawns (green circle), move towards the finish line (represented by the end of the path).
5. **Win**: Reach the exit before the ai or to stop the timer and see if you set a new record!
6. **Save**: After finishing a Time Trial Maze, you can save it to play again later.

## License

This project is licensed under the MIT License - see the LICENSE file for details (if applicable).
