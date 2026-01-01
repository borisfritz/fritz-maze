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

def save_maze_to_library(maze, timer):
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

    if not maze.name:
        maze.name = new_file_name(maze.difficulty)
    if maze.name in library:
        current_best = library[maze.name].get("best_time")
        if timer.final_time < current_best:
            library[maze.name]["best_time"] = timer.final_time
    else:
        grid_data = [[1 if cell.is_wall else 0 for cell in row] for row in maze.grid]
        library[maze.name] = {
            "grid_size" : maze.grid_size,
            "cell_size" : maze.cell_size,
            "start_pos_x" : maze.start_cell.x,
            "start_pos_y" : maze.start_cell.y,
            "end_pos_x" : maze.end_cell.x,
            "end_pos_y" : maze.end_cell.y,
            "best_time" : timer.final_time,
            "grid_data" : grid_data
        }
    os.makedirs("saves", exist_ok=True)
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)
    print(f"Maze {maze.name} saved!")

def new_file_name(difficulty):
    maze_names = get_maze_names()
    if not maze_names:
        return f"maze_1_{difficulty.value}"
    return f"maze_{len(maze_names) + 1}_{difficulty.value}"