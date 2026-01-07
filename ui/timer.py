import pygame

from constants import *

class Timer:
    def __init__(self, time):
        self.start_time = time
        self.final_time = 0
        self.is_stopped = False
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)
        self.maze_margin_x = 0
        self.maze_margin_y = 0

    def stop_time(self):
        self.is_stopped = True
        self.final_time = (pygame.time.get_ticks() - self.start_time) / 1000

    def draw(self, screen, maze):
        elapsed_time = self.final_time if self.is_stopped else (pygame.time.get_ticks() - self.start_time) / 1000
        self._draw_timer_ui(screen, maze, elapsed_time)

    def _draw_timer_ui(self, screen, maze, time_to_display):
        timer_text = self.font.render(f"Time: {time_to_display:.2f}", True, WHITE)
        center_x = maze.margin_x - 100
        center_y = maze.margin_y + maze.start_cell.y * maze.cell_size + 12
        timer_rect = timer_text.get_rect(center=(center_x, center_y))
        timer_border = timer_rect.inflate(BORDER_PADDING, BORDER_PADDING)
        pygame.draw.rect(screen, GREEN, timer_border, 5, border_radius=BORDER_RADIUS)
        screen.blit(timer_text, timer_rect)