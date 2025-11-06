import pygame
import sys

from constants import *
from maze.mazegenerator import MazeGenerator

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fritz Maze")

def main():
    maze = MazeGenerator(GRID_SIZE)

    # Game States
    STATE_GENERATING = 0
    STATE_PLAYING = 1
    STATE_WON = 2

    game_state = STATE_GENERATING
    maze.start_generation()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game_state == STATE_GENERATING:
            for _ in range(GENERATION_SPEED):
                maze.generation_step()
            if maze.generation_complete:
                game_state = STATE_PLAYING

        screen.fill(BLACK)
        maze.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()