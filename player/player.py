import pygame

from constants import PLAYER_SIZE, PLAYER_SPEED, PLAYER_COLOR, MARGIN


class Player:
    def __init__(self, start_cell):
        self.x = MARGIN + start_cell.x * start_cell.size + start_cell.size // 2
        self.y = start_cell.y * start_cell.size + start_cell.size // 2
        self.size = PLAYER_SIZE  # radius
        self.speed = PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), self.size)

    def update(self, grid):
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

        new_x = self.x + dx
        new_y = self.y + dy

        if not self.collides_with_walls(new_x, new_y, grid):
            self.x = new_x
            self.y = new_y

    def collides_with_walls(self, x, y, grid):
        if x - self.size < MARGIN:
            return True
        if x + self.size > MARGIN + grid.grid_size * grid.cell_size:
            return True
        if y - self.size < 0:
            return True
        if y + self.size > grid.grid_size * grid.cell_size:
            return True

        min_col = int((x - self.size - MARGIN) / grid.cell_size)
        max_col = int((x + self.size - MARGIN) / grid.cell_size)
        min_row = int((y - self.size) / grid.cell_size)
        max_row = int((y + self.size) / grid.cell_size)

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                cell = grid.get_cell(col, row)
                if cell and cell.is_wall:
                    return True
        return False
