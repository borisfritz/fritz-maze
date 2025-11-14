import pygame

from constants import *

class Cell:
    def __init__(self, x, y, cell_size, margin_x=0, margin_y=0):
        self.x = x
        self.y = y
        self.size = cell_size
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.visited = False
        self.is_wall = True

    def draw(self, screen, color=None):
        if color is None:
            color = WALL_COLOR if self.is_wall else PATH_COLOR

        rect = pygame.Rect(
            self.margin_x + self.x * self.size,
            self.margin_y + self.y * self.size,
            self.size,
            self.size
        )
        pygame.draw.rect(screen, color, rect)
        #pygame.draw.rect(screen, BLACK, rect, 1)