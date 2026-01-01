import pygame
import sys

from constants import *
from maze.maze import Maze
from player.player import Player
from ui.game_text import draw_start_text
from ui.timer import Timer
from ui.menus import draw_main_menu, draw_tt_menu, draw_vs_menu, draw_victory_menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fritz Maze")
        self.is_running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.frame_rate = 0
        self.font = pygame.font.Font(None, 48)
        self.game_state = GameState.MENU
        self.menu_state = MenuState.MAIN
        self.maze = None
        self.difficulty = None
        self.player = None
        self.timer = None
        self.window = None
        self.game_mode = None

    def play(self):
        while self.is_running:
            pos = pygame.mouse.get_pos()
            action = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    print("Exiting Game via Quit")
                if event.type == pygame.MOUSEBUTTONDOWN and self.window:
                    action = self.window.get_button_clicked(pos)

            self.screen.fill(BLACK)
            self.display_state(pos)
            if self.maze:
                self.maze.draw(self.screen)
            if self.player is not None:
                self.player.draw(self.screen)
            if self.timer is not None:
                self.timer.draw(self.screen, self.maze)
            if self.game_state == GameState.FINISHED:
                self.window = draw_victory_menu(self.screen, self.font, pos, self.timer)

            if action:
                self.set_action(action)

            pygame.display.flip()
            self.frame_rate = self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def display_state(self, pos):
        match self.game_state:
            case GameState.MENU:
                match self.menu_state:
                    case MenuState.MAIN:
                        self.window = draw_main_menu(self.screen, self.font, pos)
                    case MenuState.TT_MENU:
                        self.window = draw_tt_menu(self.screen, self.font, pos)
                    case MenuState.VS_MENU:
                        self.window = draw_vs_menu(self.screen, self.font, pos)
            case GameState.CREATE_MAZE:
                self.maze = Maze(self.difficulty)
                self.maze.start_generation()
                print(f"Generating {self.difficulty.value} Maze")
                self.game_state = GameState.GENERATE_MAZE
            case GameState.GENERATE_MAZE:
                for _ in range(GENERATION_SPEED):
                    self.maze.generation_step()
                if self.maze.generation_complete:
                    print("Generation complete")
                    self.game_state = GameState.SPAWN_PLAYER
            case GameState.SPAWN_PLAYER:
                self.player = Player(self.maze)
                print("Player Spawned")
                self.game_state = GameState.PLAYING
                print("Time Trial Mode Started")
            case GameState.PLAYING:
                if self.game_mode == GameMode.TIME_TRIAL:
                    self.player.update(self.maze)
                    if not self.player.has_started and self.timer is None:
                        draw_start_text(self.screen, self.maze)
                    elif self.player.has_started and self.timer is None:
                        self.timer = Timer(pygame.time.get_ticks())
                        print("Timer Started")
                    if self.player.won:
                        self.timer.stop_time()
                        self.game_state = GameState.FINISHED
                        print(f"Timer Stopped at {self.timer.final_time:.2f} seconds")
                if self.game_mode == GameMode.VERSES:
                    pass

    def set_action(self, action):
        match action:
            case Action.SET_MAIN_MENU:
                self.maze = None
                self.player = None
                self.timer = None
                self.game_mode = None
                self.game_state = GameState.MENU
                self.menu_state = MenuState.MAIN
            case Action.SET_TT_MENU:
                self.menu_state = MenuState.TT_MENU
                self.game_mode = GameMode.TIME_TRIAL
            case Action.SET_VS_MENU:
                pass
                #self.menu_state = MenuState.VS_MENU
            case Action.SET_LOAD_MENU:
                pass
                #load maze
            case Action.GEN_EASY_MAZE:
                self.window = None
                self.difficulty = GameDifficulty.EASY
                self.game_state = GameState.CREATE_MAZE
            case Action.GEN_MEDIUM_MAZE:
                self.window = None
                self.difficulty = GameDifficulty.MEDIUM
                self.game_state = GameState.CREATE_MAZE
            case Action.GEN_HARD_MAZE:
                self.window = None
                self.difficulty = GameDifficulty.HARD
                self.game_state = GameState.CREATE_MAZE
            case Action.RETRY:
                self.player = None
                self.window = None
                self.timer = None
                print("Re-starting Game at player spawning")
                self.game_state = GameState.SPAWN_PLAYER
            case Action.EXIT:
                self.is_running = False
                print("Exiting Game")

def main():
    print("Starting Game at Main Menu!  Welcome!")
    game = Game()
    game.play()

if __name__ == "__main__":
    main()