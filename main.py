import pygame
import sys

from enum import Enum
from constants import *
from maze.maze_generator import MazeGenerator

class state(Enum):
    GENERATING = 0
    PLAYING = 1
    WON = 2

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fritz Maze")
clock = pygame.time.Clock()

def main():
    maze = MazeGenerator(GRID_SIZE)

    game_state = state.GENERATING
    maze.start_generation()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        match game_state:
            case state.GENERATING:
                for _ in range(GENERATION_SPEED):
                    maze.generation_step()
                if maze.generation_complete:
                    game_state = state.PLAYING
            case state.PLAYING:
                if maze.current.is_end:
                    game_state = state.WON

        screen.fill(BLACK)
        maze.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()