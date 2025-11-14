import pygame
import sys
from enum import Enum

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRID_SIZE, CELL_SIZE, FPS, GENERATION_SPEED
from maze.maze_generator import MazeGenerator
from player.player import Player

class GameState(Enum):
    GENERATE_MAZE = "generate maze"
    SPAWN_PLAYER = "spawn player"
    PLAY_VERSES = "playing verses"
    WON = "won"
    LOST = "lost"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fritz Maze")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.ms = 0
        self.dt = 0

    def run(self):
        maze = MazeGenerator(GRID_SIZE, CELL_SIZE)
        game_state = GameState.GENERATE_MAZE
        player = None
        maze.start_generation()
        print("Started generation")

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear screen at the start of the frame
            self.screen.fill(BLACK)

            match game_state:
                case GameState.GENERATE_MAZE:
                    for _ in range(GENERATION_SPEED):
                        maze.generation_step()
                    if maze.generation_complete:
                        print("Generation complete")
                        game_state = GameState.SPAWN_PLAYER
                case GameState.SPAWN_PLAYER:
                    player = Player(maze.start_cell)
                    print("Spawned player")
                    game_state = GameState.PLAY_VERSES
                case GameState.PLAY_VERSES:
                    player.update()

            # Draw world
            maze.draw(self.screen)
            if player is not None:
                player.draw(self.screen)

            pygame.display.flip()
            self.ms = self.clock.tick(FPS)
            self.dt = self.ms / 1000
        pygame.quit()
        sys.exit()

Game().run()