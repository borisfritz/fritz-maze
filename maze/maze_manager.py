import pickle
import os

def save_maze(maze):
    os.makedirs("saves", exist_ok=True)

    with open(f"saves/{maze.name}.pkl", "wb") as f:
        pickle.dump(maze, f)

# WARNING: Pickle is used for serialization due to complex graph data (cell neighbor references).
# Only load save files you created yourself - pickle can execute arbitrary code from malicious files.
def load_maze(name):
    name_split = name.split(".")
    if len(name_split) != 2 or name_split[-1] != "pkl":
        raise ValueError(f"Invalid Maze Name: {name}")
    maze_name = name_split[0]
    try:
        with open(f"saves/{maze_name}.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Maze {name} not found!")
        return None

def get_saved_mazes():
    os.makedirs("saves", exist_ok=True)
    return os.listdir("saves")