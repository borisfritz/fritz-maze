import pygame
from constants import *

def draw_text(screen, text, font, col, x, y):
    img = font.render(text, True, col)
    screen.blit(img, (x, y))

def draw_start_text(screen, maze):
    start_pos_x = maze.margin_x - 110
    start_pos_y = maze.margin_y + maze.start_cell.y * maze.cell_size
    font = pygame.font.Font(None, 40)
    draw_text(screen,'START', font, GREEN, start_pos_x, start_pos_y)

def draw_finish_text(screen, maze):
    start_pos_x = maze.margin_x + maze.end_cell.x * maze.cell_size + 30
    start_pos_y = maze.margin_y + maze.end_cell.y * maze.cell_size
    font = pygame.font.Font(None, 40)
    draw_text(screen,'FINISH!', font, BLUE, start_pos_x, start_pos_y)