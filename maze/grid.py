import pygame

from constants import *

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_wall = True
        self.visited = False
        self.is_active = False
        self.is_start = False
        self.is_finish = False
        self.neighbors = []

    def get_color(self):
        if self.is_active:
            return RED
        if self.is_start:
            return DARK_GREEN
        if self.is_finish:
            return DARK_BLUE
        if self.is_wall:
            return WHITE
        return DARK_GRAY

class Grid:
    def __init__(self, width, height, cell_size, margin_x=0, margin_y=0):
        self.width = width
        self.height = height
        self.size = cell_size
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.cells = {(x, y): Cell(x, y) for x in range(width) for y in range(height)}

    def get_cell(self, x, y):
        return self.cells.get((x, y))

    def get_unvisited_neighbors(self, cell):
        unvisited_neighbors = []
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        for dx, dy in directions:
            neighbor = self.get_cell(cell.x + dx, cell.y + dy)
            if neighbor and not neighbor.visited:
                mid_cell = self.get_cell(cell.x + dx // 2, cell.y + dy // 2)
                unvisited_neighbors.append((mid_cell, neighbor))
        return unvisited_neighbors

    def add_path(self, cell_1, cell_2):
        cell_1.neighbors.append(cell_2)
        cell_2.neighbors.append(cell_1)

    def draw(self, screen):
        for cell in self.cells.values():
            color = cell.get_color()
            rect = pygame.Rect(
                self.margin_x + cell.x * self.size,
                self.margin_y + cell.y * self.size,
                self.size,
                self.size
            )
            pygame.draw.rect(screen, color, rect)