import pygame

from constants import *

class Player:
    def __init__(self, maze, color=GREEN):
        self.margin_x, self.margin_y = calculate_margins(maze.grid_size, maze.cell_size)
        self.x = self.margin_x + maze.start_cell.x * maze.cell_size + maze.cell_size // 2
        self.y = self.margin_y + maze.start_cell.y * maze.cell_size + maze.cell_size // 2
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.color = color
        self.start_x = self.x
        self.start_y = self.y
        self.has_started = False
        self.won = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def get_current_cell(self, maze):
        curr_col = int((self.x - self.margin_x) / maze.cell_size)
        curr_row = int((self.y - self.margin_y) / maze.cell_size)
        return maze.grid.get_cell(curr_col, curr_row)

    def update(self, maze, ai_direction=None):
        if self.start_x != self.x or self.start_y != self.y:
            self.has_started = True
        if ai_direction:
            dx, dy = ai_direction
        else:
            dx, dy = self._handle_input()
        if dx != 0 and not self.collides_with_walls(self.x + dx, self.y, maze):
            self.x += dx
        if dy != 0 and not self.collides_with_walls(self.x, self.y + dy, maze):
            self.y += dy
        self._check_win_condition(maze)

    def collides_with_walls(self, x, y, maze):
        maze_width = maze.grid_size * maze.cell_size
        if not (self.margin_x + self.size <= x <= self.margin_x + maze_width - self.size and
                self.margin_y + self.size <= y <= self.margin_y + maze_width - self.size):
            return True

        current_cell = self.get_current_cell(maze)
        if not current_cell:
            return True

        min_col = int((x - self.size - self.margin_x) / maze.cell_size)
        max_col = int((x + self.size - self.margin_x) / maze.cell_size)
        min_row = int((y - self.size - self.margin_y) / maze.cell_size)
        max_row = int((y + self.size - self.margin_y) / maze.cell_size)

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                target_cell = maze.grid.get_cell(col, row)
                if not target_cell or (target_cell != current_cell and target_cell not in current_cell.neighbors):
                    return True
        return False

    def _check_win_condition(self, maze):
        current_cell = self.get_current_cell(maze)
        if current_cell.is_finish:
            self.won = True

    def _handle_input(self):
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
        return dx, dy