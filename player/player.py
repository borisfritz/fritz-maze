import pygame

from constants import *

class Player:
    def __init__(self, start_cell, grid_size, cell_size):
        # Initialize player location and stats
        self.margin_x, self.margin_y = calculate_margins(grid_size, cell_size)
        self.x = self.margin_x + start_cell.x * start_cell.size + start_cell.size // 2
        self.y = self.margin_y + start_cell.y * start_cell.size + start_cell.size // 2
        self.size = PLAYER_SIZE  # radius
        self.speed = PLAYER_SPEED
        # checks to see when player starts moving to start the mode
        self.start_x = self.x
        self.start_y = self.y
        self.has_started = False
        # checks to see if player has won the game
        self.won = False

    def draw(self, screen):
        pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), self.size)

    def update(self, grid):
        if self.start_x != self.x or self.start_y != self.y:
            self.has_started = True
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += self.speed

        if dx != 0:
            new_x = self.x + dx
            if not self.collides_with_walls(new_x, self.y, grid):
                self.x = new_x
        if dy != 0:
            new_y = self.y + dy
            if not self.collides_with_walls(self.x, new_y, grid):
                self.y = new_y

    def collides_with_walls(self, x, y, grid):
        if x - self.size < self.margin_x:
            return True
        if x + self.size > self.margin_x + grid.grid_size * grid.cell_size:
            return True
        if y - self.size < self.margin_y:
            return True
        if y + self.size > self.margin_y + grid.grid_size * grid.cell_size:
            return True

        min_col = int((x - self.size - self.margin_x) / grid.cell_size)
        max_col = int((x + self.size - self.margin_x) / grid.cell_size)
        min_row = int((y - self.size - self.margin_y) / grid.cell_size)
        max_row = int((y + self.size - self.margin_y) / grid.cell_size)

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                cell = grid.get_cell(col, row)
                if cell and cell.is_wall:
                    return True
                if cell and cell.is_finish:
                    self.won = True
        return False
