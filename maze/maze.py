import random
from unittest import case

from constants import *
from maze.grid import Grid
from ui.game_text import draw_finish_text


class Maze:
    def __init__(self, difficulty):
        self.name = None
        self.difficulty = difficulty
        self.grid_size = self._set_grid_size()
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
        self._visit_cell(start_cell)
        self.current = start_cell
        self.stack = [start_cell]
        self.generating = True
        self.generation_complete = False

    def generation_step(self):
        if not self.generating or self.generation_complete:
            return
        if self.current:
            self.current.is_active = False
        if self.stack:
            self.current = self.stack[-1]
            self.current.is_active = True
            unvisited_neighbors = self.grid.get_unvisited_neighbors(self.current)
            if unvisited_neighbors:
                mid_cell, next_cell = random.choice(unvisited_neighbors)
                self.grid.add_path(self.current, mid_cell)
                self.grid.add_path(mid_cell, next_cell)
                self._visit_cell(mid_cell)
                self._visit_cell(next_cell)
                self.stack.append(next_cell)
            else:
                self.stack.pop()
        else:
            self.generate_start_finish_cells()
            self.generating = False
            self.generation_complete = True
            self.current = False

    def generate_start_finish_cells(self):
        self._initialize_special_cell(0, 1, is_start=True)
        self._initialize_special_cell(self.grid_size - 1, self.grid_size - 2, is_start=False)

    def draw(self, screen):
        if self.grid:
            self.grid.draw(screen)
        if self.end_cell:
            draw_finish_text(screen, self)

    def _visit_cell(self, cell):
        cell.visited = True
        cell.is_wall = False

    def _set_grid_size(self):
        match self.difficulty:
            case GameDifficulty.EASY:
                return GRID_SIZE_EASY
            case GameDifficulty.MEDIUM:
                return GRID_SIZE_MEDIUM
            case GameDifficulty.HARD:
                return GRID_SIZE_HARD
        return GRID_SIZE_EASY

    def _initialize_special_cell(self, x, check_x, is_start=True):
        while True:
            y = random.randint(1, self.grid_size - 1)
            check_cell = self.grid.get_cell(check_x, y)
            if not check_cell.is_wall:
                special_cell = self.grid.get_cell(x, y)
                self._visit_cell(special_cell)
                if is_start:
                    special_cell.is_start = True
                    self.start_cell = special_cell
                else:
                    special_cell.is_finish = True
                    self.end_cell = special_cell
                self.grid.add_path(special_cell, check_cell)
                return