import json
import os

from constants import *
from maze.cell import Cell

def get_maze_names():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, "r") as f:
        library = json.load(f)
    return list(library.keys())

def save_maze_to_library(maze, timer=None):
    if not maze.generation_complete:
        print("Maze not generated yet!")
        return

    library = {}
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            try:
                library = json.load(f)
            except json.JSONDecodeError:
                library = {}
                print("Error loading library file!")

    grid_data = [[1 if cell.is_wall else 0 for cell in row] for row in maze.grid]

    maze_entry = {
        "grid_size" : maze.grid_size,
        "cell_size" : maze.cell_size,
        "start_pos" : (maze.start_cell.x, maze.start_cell.y),
        "end_pos" : (maze.end_cell.x, maze.end_cell.y),
        "best_time" : timer.final_time if timer else None,
        "grid_data" : grid_data
    }

    maze_name = new_file_name(maze.difficulty)
    library[maze_name] = maze_entry

    os.makedirs("saves", exist_ok=True)
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)
    print(f"Maze {maze_name} saved!")

def new_file_name(difficulty):
    maze_names = get_maze_names()
    if not maze_names:
        return f"maze_1 : {difficulty.value}"
    return f"maze_{len(maze_names) + 1} : {difficulty.value}"