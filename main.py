from unittest import case

import pygame
import sys

from constants import *
from maze.maze_generator import MazeGenerator
from player.player import Player
from ui.game_text import draw_start_text
from ui.timer import Timer
from ui.victory_screen import draw_victory_screen

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fritz Maze")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.frame_rate = 0
        self.font = pygame.font.Font(None, 48)

    def menu(self):
        pass

    def play(self, game_mode, maze_difficulty, vs_difficulty=None):
        maze = None
        match maze_difficulty:
            case GameDifficulty.EASY:
                maze = MazeGenerator(GRID_SIZE_EASY, CELL_SIZE)
            case GameDifficulty.MEDIUM:
                maze = MazeGenerator(GRID_SIZE_MEDIUM, CELL_SIZE)
            case GameDifficulty.HARD:
                maze = MazeGenerator(GRID_SIZE_HARD, CELL_SIZE)

        player = None
        timer = None
        victory_screen = None

        game_state = GameState.GENERATE_MAZE
        maze.start_generation()
        print("Started generation")

        # Game loop
        running = True
        while running:
            pos = pygame.mouse.get_pos()
            action = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and victory_screen:
                    action = victory_screen.get_button_clicked(pos)

            self.screen.fill(BLACK)

            match game_state:
                case GameState.GENERATE_MAZE:
                    for _ in range(GENERATION_SPEED):
                        maze.generation_step()
                    if maze.generation_complete:
                        print("Generation complete")
                        game_state = GameState.SPAWN_PLAYER

                case GameState.SPAWN_PLAYER:
                    player = Player(maze)
                    print("Player Spawned")
                    game_state = GameState.PLAYING
                    print("Time Trial Mode Started")

                case GameState.PLAYING:
                    if game_mode == GameMode.TIME_TRIAL:
                        player.update(maze)
                        if not player.has_started and timer is None:
                            draw_start_text(self.screen, maze)
                        elif player.has_started and timer is None:
                            timer = Timer(pygame.time.get_ticks())
                            print("Timer Started")
                        if player.won:
                            timer.stop_time()
                            game_state = GameState.FINISHED
                            print("Timer Stopped")
                    if game_mode == GameMode.VERSES:
                        pass

            maze.draw(self.screen)
            if player is not None:
                player.draw(self.screen)
            if timer is not None:
                timer.draw(self.screen, maze)
            if game_state == GameState.FINISHED:
               victory_screen = draw_victory_screen(self.screen, self.font, timer, pos)

            if action:
                match action:
                    case Action.RETRY:
                        player = None
                        victory_screen = None
                        timer = None
                        print("Re-starting Game at player spawning")
                        game_state = GameState.SPAWN_PLAYER
                    case Action.EXIT:
                        running = False
                        print("Exiting Game")

            pygame.display.flip()
            self.frame_rate = self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game_screen = GameScreen.GAME
    game_mode = GameMode.TIME_TRIAL
    game_difficulty = GameDifficulty.EASY
    match game_screen:
        case GameScreen.GAME:
            game.play(game_mode, game_difficulty)

if __name__ == "__main__":
    main()