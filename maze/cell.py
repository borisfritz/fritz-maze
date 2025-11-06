import pygame

from constants import *

class Cell:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.size = CELL_SIZE
        self.visited = False
        self.is_wall = True

    def draw(self, screen, color=None):
        if color is None:
            color = WALL_COLOR if self.is_wall else PATH_COLOR

        rect = pygame.Rect(
            MARGIN + self.x * self.size,
            MARGIN + self.y * self.size,
            self.size,
            self.size
        )
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)