import json
import os
import re

from constants import *
from maze.maze import Maze

def get_saved_mazes():
    library = {}
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            try:
                library = json.load(f)
            except json.JSONDecodeError:
                library = {}
                print("Error loading library file!")
    return list(library.keys())

def save_maze_to_library(maze, new_time):
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
        maze.name = f"Maze_{len(library) + 1}_{maze.difficulty.value}"
    if maze.name in library:
        current_best = library[maze.name].get("best_time")
        if new_time < current_best:
            library[maze.name]["best_time"] = new_time
            print(f"New best time for {maze.name}: {new_time}")
    else:
        grid_data = [[1 if cell.is_wall else 0 for cell in row] for row in maze.grid]
        library[maze.name] = {
            "grid_size" : maze.grid_size,
            "cell_size" : maze.cell_size,
            "start_pos_x" : maze.start_cell.x,
            "start_pos_y" : maze.start_cell.y,
            "end_pos_x" : maze.end_cell.x,
            "end_pos_y" : maze.end_cell.y,
            "best_time" : new_time,
            "grid_data" : grid_data
        }

    os.makedirs("saves", exist_ok=True)
    json_string = json.dumps(library, indent=4)
    # Remove extra lines from JSON string
    compact_json = re.sub(r'\n +([0-9-\]])', r' \1', json_string)
    with open(LIBRARY_FILE, "w") as f:
        f.write(compact_json)
    print(f"Maze {maze.name} saved!")

def load_maze_from_library(name):
    # Load Library File
    if not os.path.exists(LIBRARY_FILE):
        print("Library file not found!")
        return None
    try:
        with open(LIBRARY_FILE, "r") as f:
            library = json.load(f)
    except json.JSONDecodeError:
        print("Error loading library file!")
        return None
    if name not in library:
        print(f"Maze {name} not found in library!")
        return None
    # Reconstruct Maze
    data = library[name]
    difficulty_str = name.split("_")[-1]
    if difficulty_str == "Easy":
        difficulty = GameDifficulty.EASY
    elif difficulty_str == "Medium":
        difficulty = GameDifficulty.MEDIUM
    elif difficulty_str == "Hard":
        difficulty = GameDifficulty.HARD
    else:
        print(f"Unknown difficulty: {difficulty_str}")
        return None
    maze = Maze(difficulty)
    maze.name = name
    maze.start_cell = maze.get_cell(data["start_pos_x"], data["start_pos_y"])
    maze.end_cell = maze.get_cell(data["end_pos_x"], data["end_pos_y"])
    if maze.end_cell:
        maze.end_cell.is_finish = True
    grid_data = data["grid_data"]
    for x in range(maze.grid_size):
        for y in range(maze.grid_size):
            cell = maze.get_cell(x, y)
            if cell:
                cell.is_wall = bool(grid_data[x][y])
                cell.visited = True
    maze.best_time = data["best_time"]
    maze.generation_complete = True
    maze.generating = False
    return maze