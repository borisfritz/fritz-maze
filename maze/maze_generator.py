import random

from constants import CURRENT_COLOR, START_COLOR, END_COLOR
from maze.cell import Cell

class MazeGenerator:
    def __init__(self, grid_size, cell_size):
        self.grid_size = grid_size
        self.grid = [[Cell(x, y, cell_size) for y in range(self.grid_size)] for x in range(self.grid_size)]
        self.stack = []
        self.current = None
        self.start_cell = False
        self.end_cell = False
        self.generating = False
        self.generation_complete = False

    def get_cell(self, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        return None

    def get_unvisited_neighbors(self, cell):
        neighbors = []
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)] # up, right, down, left
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            neighbor = self.get_cell(nx, ny)
            if neighbor and not neighbor.visited:
                neighbors.append((neighbor, dx // 2, dy // 2))
        return neighbors

    def start_generation(self):
        start_cell = self.grid[1][1]
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
            neighbors = self.get_unvisited_neighbors(self.current)
            if neighbors:
                next_cell, dx, dy = random.choice(neighbors)
                wall_x = self.current.x + dx
                wall_y = self.current.y + dy
                wall = self.get_cell(wall_x, wall_y)
                if wall:
                    wall.is_wall = False
                    wall.visited = True
                next_cell.visited = True
                next_cell.is_wall = False
                self.stack.append(next_cell)
            else:
                self.stack.pop()
        else:
            self.generate_start_finish_cells()
            self.generating = False
            self.generation_complete = True

    def generate_start_finish_cells(self):
        start_set = False
        while not start_set:
            a = random.randint(1, self.grid_size - 1)
            if not self.grid[1][a].is_wall:
                start = self.grid[0][a]
                start.is_wall = False
                start.visited = True
                self.start_cell = start
                start_set = True
        end_set = False
        while not end_set:
            b = random.randint(1, self.grid_size - 1)
            if not self.grid[self.grid_size - 2][b].is_wall:
                end = self.grid[self.grid_size - 1][b]
                end.is_wall = False
                end.visited = True
                self.end_cell = end
                end_set = True

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

        if self.generating and self.current:
            self.current.draw(screen, CURRENT_COLOR)
        if self.start_cell:
            self.start_cell.draw(screen, START_COLOR)
        if self.end_cell:
            self.end_cell.draw(screen, END_COLOR)