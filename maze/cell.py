import pygame

from constants import *

class Cell:
    def __init__(self, x, y, cell_size, color=None):
        self.x = x
        self.y = y
        self.size = cell_size
        self.visited = False
        self.is_wall = True
        ###
        self.is_start = False
        self.is_end = False

    def draw(self, screen, color=None):
        if color is None:
            color = WALL_COLOR if self.is_wall else PATH_COLOR

        rect = pygame.Rect(
            MARGIN + self.x * self.size,
            self.y * self.size,
            self.size,
            self.size
        )
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)