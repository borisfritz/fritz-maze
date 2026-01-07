import pickle
import os
import re

from constants import *
from maze.maze import Maze

def save_maze(maze):
    os.makedirs("saves", exist_ok=True)

    with open(f"saves/{maze.name}.pkl", "wb") as f:
        pickle.dump(maze, f)

def load_maze(name):
    try:
        with open(f"saves/{name}", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Maze {name} not found!")
        return None

def get_saved_mazes():
    return os.listdir("saves")