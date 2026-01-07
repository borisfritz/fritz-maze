import random

from constants import *
from maze.cell import Grid
from ui.game_text import draw_finish_text


class Maze:
    def __init__(self, difficulty):
        self.name = None
        self.difficulty = difficulty
        match self.difficulty:
            case GameDifficulty.EASY:
                self.grid_size = GRID_SIZE_EASY
            case GameDifficulty.MEDIUM:
                self.grid_size = GRID_SIZE_MEDIUM
            case GameDifficulty.HARD:
                self.grid_size = GRID_SIZE_HARD
        self.cell_size = CELL_SIZE
        self.margin_x, self.margin_y = calculate_margins(self.grid_size, self.cell_size)
        self.grid = Grid(self.grid_size, self.grid_size, self.cell_size, self.margin_x, self.margin_y)
        self.stack = []
        self.current = None
        self.generating = False
        self.generation_complete = False
        self.start_cell = False
        self.end_cell = False
        self.best_time = None

    def start_generation(self):
        start_cell = self.grid.get_cell(1,1)
        start_cell.visited = True
        start_cell.is_wall = False
        self.current = start_cell
        self.stack = [start_cell]
        self.generating = True
        self.generation_complete = False

    def generation_step(self):
        if not self.generating or self.generation_complete:
            return
        if self.stack:
            self.current = self.stack[-1]
            unvisited_neighbors = self.grid.get_unvisited_neighbors(self.current)
            if unvisited_neighbors:
                mid_cell, next_cell = random.choice(unvisited_neighbors)
                self.grid.add_path(self.current, mid_cell)
                self.grid.add_path(mid_cell, next_cell)
                mid_cell.is_wall = False
                mid_cell.visited = True
                next_cell.is_wall = False
                next_cell.visited = True
                self.stack.append(next_cell)
            else:
                self.stack.pop()
        else:
            self.generate_start_finish_cells()
            self.generating = False
            self.generation_complete = True
            self.current = False

    def generate_start_finish_cells(self):
        start_set = False
        while not start_set:
            a = random.randint(1, self.grid_size - 1)
            check_a = self.grid.get_cell(1,a)
            if not check_a.is_wall:
                start = self.grid.get_cell(0, a)
                start.is_wall = False
                start.visited = True
                start.is_start = True
                self.grid.add_path(start, check_a)
                self.start_cell = start
                start_set = True
        end_set = False
        while not end_set:
            b = random.randint(1, self.grid_size - 1)
            check_b = self.grid.get_cell(self.grid_size - 2, b)
            if not check_b.is_wall:
                end = self.grid.get_cell(self.grid_size - 1, b)
                end.is_wall = False
                end.visited = True
                end.is_finish = True
                self.grid.add_path(end, check_b)
                self.end_cell = end
                end_set = True


    def draw(self, screen):
        if self.grid:
            self.grid.draw(screen)
        if self.end_cell:
            draw_finish_text(screen, self)