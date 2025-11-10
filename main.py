import pygame
import sys
from enum import Enum

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRID_SIZE, CELL_SIZE, FPS, GENERATION_SPEED
from maze.maze_generator import MazeGenerator

class GameState(Enum):
    GENERATING = "generating"
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fritz Maze")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        maze = MazeGenerator(GRID_SIZE, CELL_SIZE)
        game_state = GameState.GENERATING
        maze.start_generation()

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            match game_state:
                case GameState.GENERATING:
                    for _ in range(GENERATION_SPEED):
                        maze.generation_step()
                    if maze.generation_complete:
                        game_state = GameState.PLAYING
                case GameState.PLAYING:
                    pass

            self.screen.fill(BLACK)
            maze.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

Game().run()