# Fritz Maze

A fun and challenging maze game built with Python and Pygame. Navigate through randomly generated mazes, beat the clock in Time Trial mode, and save your favorite mazes to challenge yourself later.

## Features

- **Random Maze Generation**: Every game is unique!
- **Difficulty Levels**: Choose between Easy, Medium, and Hard.
- **Time Trial Mode**: Race against the clock and set new records.
- **Save & Load**: Save generated mazes and reload them anytime.
- **Cross-Platform**: Works on both Windows and Linux.

## Prerequisites

- **Python**: Version 3.13 or higher is recommended.
- **uv** (Optional but recommended): A fast Python package manager.

## Installation

### Using uv (Recommended)

If you have `uv` installed, you can run the game directly:

```bash
uv run main.py
```

### Using pip

1. Clone or download the repository.
2. Navigate to the project directory:
   ```bash
   cd fritz-maze
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## How to Run

### Windows

1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the project folder.
3. Run the game:
   ```powershell
   python main.py
   ```

### Linux

1. Open your **Terminal**.
2. Navigate to the project folder.
3. Ensure you have the necessary dependencies for Pygame (may vary by distribution, e.g., `sudo apt-get install python3-pygame`).
4. Run the game:
   ```bash
   python3 main.py
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
