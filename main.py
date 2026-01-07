import pygame
import sys

from maze.maze import Maze
from player.player import Player
from ui.game_text import draw_start_text
from ui.timer import Timer
from ui.menus import *
from maze.maze_manager import save_maze, load_maze, get_saved_mazes

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
            events = pygame.event.get()
            pos = pygame.mouse.get_pos()
            self.handle_events(events, pos)
            self.update(pos)
            self.draw(pos)
            pygame.display.flip()
            self.frame_rate = self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self, events, pos):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
                print("Exiting Game via Quit")
            if event.type == pygame.MOUSEBUTTONDOWN and self.window:
                if event.button == 1:
                    button = self.window.get_button_clicked(pos)
                    if button:
                        self._process_action(button)
            if event.type == pygame.MOUSEWHEEL and self.window and self.window.buttons:
                if event.y > 0:
                    self.window.current_page = max(0, self.window.current_page - 1)
                elif event.y < 0:
                    max_pages = (len(self.window.buttons) - 1) // self.window.max_per_page
                    self.window.current_page = min(max_pages, self.window.current_page + 1)

    def update(self, pos):
        match self.game_state:
            case GameState.MENU:
                self._update_menu(pos)
            case GameState.CREATE_MAZE:
                self._init_maze_generation()
            case GameState.GENERATE_MAZE:
                self._step_maze_generation()
            case GameState.SPAWN_PLAYER:
                self._spawn_player()
            case GameState.PLAYING:
                self._update_playing_state(pos)

    def draw(self, pos):
        self.screen.fill(BLACK)
        if self.window:
            self.window.draw(self.screen, self.font, pos, WHITE)
        if self.maze:
            self.maze.draw(self.screen)
        if self.player:
            self.player.draw(self.screen)
        if self.timer:
            self.timer.draw(self.screen, self.maze)
        if self.game_state == GameState.PLAYING and not self.player.has_started:
            draw_start_text(self.screen, self.maze)
        if self.game_state == GameState.FINISHED and self.window:
            self.window.draw(self.screen, self.font, pos, WHITE)

    def _process_action(self, button):
        action = button.action
        match action:
            case Action.SET_MAIN_MENU:
                self._reset_game_elements()
                self.game_mode = None
                self.game_state = GameState.MENU
                self.menu_state = MenuState.MAIN
            case Action.SET_TT_MENU:
                self.menu_state = MenuState.TT_MENU
                self.game_mode = GameMode.TIME_TRIAL
                self.window = None
            case Action.SET_VS_MENU:
                pass
            case Action.SET_LOAD_MENU:
                self.menu_state = MenuState.LOAD_MENU
                self.window = None
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
            case Action.SAVE_MAZE:
                self.maze.name = f"{self.difficulty.value}_{len(get_saved_mazes()) + 1}"
                save_maze(self.maze)
                self.window.text = "Maze Saved!"
            case Action.LOAD_MAZE:
                self.maze = load_maze(button.text)
                self._reset_game_elements(reset_maze=False)
                print(f"Loaded maze: {button.text}")
                self.game_state = GameState.SPAWN_PLAYER
            case Action.RETRY:
                self._reset_game_elements(reset_maze=False)
                print("Re-starting Game at player spawning")
                self.game_state = GameState.SPAWN_PLAYER
            case Action.EXIT:
                self.is_running = False
                print("Exiting Game")

    def _update_menu(self, pos):
        match self.menu_state:
            case MenuState.MAIN:
                if not self.window or self.window.text != "Fritz Maze Game!":
                    self.window = main_menu(self.screen, self.font, pos)
            case MenuState.TT_MENU:
                if not self.window or self.window.text != "Time Trial":
                    self.window = tt_menu(self.screen, self.font, pos)
            case MenuState.VS_MENU:
                self.window = vs_menu(self.screen, self.font, pos)
            case MenuState.LOAD_MENU:
                if not self.window or self.window.text != "Load Maze":
                    self.window = load_menu(self.screen, self.font, pos)

    def _init_maze_generation(self):
        self.maze = Maze(self.difficulty)
        self.maze.start_generation()
        print(f"Generating {self.difficulty.value} Maze")
        self.game_state = GameState.GENERATE_MAZE

    def _step_maze_generation(self):
        for _ in range(GENERATION_SPEED):
            self.maze.generation_step()
        if self.maze.generation_complete:
            print("Generation complete")
            self.game_state = GameState.SPAWN_PLAYER

    def _spawn_player(self):
        self.player = Player(self.maze)
        print("Player Spawned")
        self.game_state = GameState.PLAYING

    def _update_playing_state(self, pos):
        if self.game_mode == GameMode.TIME_TRIAL:
            self.player.update(self.maze)
            if self.player.has_started and self.timer is None:
                self.timer = Timer(pygame.time.get_ticks())
                print("Timer Started")
            if self.player.won:
                self._handle_victory(pos)
        if self.game_mode == GameMode.VERSES:
            pass

    def _handle_victory(self, pos):
        if self.game_mode == GameMode.TIME_TRIAL:
            self.timer.stop_time()
            self.window = victory_menu(self.screen, self.font, pos, self.timer)
            print(f"Timer Stopped at {self.timer.final_time:.2f} seconds")
            is_new_record = not self.maze.best_time or self.timer.final_time < self.maze.best_time
            if is_new_record:
                self.maze.best_time = self.timer.final_time
                self.window.text = f"New Record: {self.timer.final_time:.2f} seconds!"
                if self.maze.name:
                    save_maze(self.maze)
                    print(f"New Record Time Saved")
            self.game_state = GameState.FINISHED
        if self.game_mode == GameMode.VERSES:
            pass

    def _reset_game_elements(self, reset_maze=True):
        if reset_maze:
            self.maze = None
        self.player = None
        self.timer = None
        self.window = None

def main():
    print("Starting Game at Main Menu!  Welcome!")
    game = Game()
    game.play()
    sys.exit()

if __name__ == "__main__":
    main()

# main.py - 204
# constants.py - 88
# maze.py - 95
# grid.py - 62
# maze_manager.py - 20
# player.py - 74
# window.py - 69
# button.py - 37
# timer.py - 29
# menus.py - 54
# game_text.py - 18
#
# total - 750
