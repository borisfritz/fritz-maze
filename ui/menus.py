from ui.window import Window
from ui.button import Button
from constants import *
from maze.maze_manager import get_saved_mazes

def main_menu(screen, font, pos):
    main_menu_text = "Fritz Maze Game!"
    main_menu_screen = Window(WHITE, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, main_menu_text)
    tt_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Time Trial', 32, Action.SET_TT_MENU)
    vs_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Versus', 32, Action.SET_VS_MENU)
    exit_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Exit', 32, Action.EXIT)
    main_menu_screen.add_button(tt_button)
    main_menu_screen.add_button(vs_button)
    main_menu_screen.add_button(exit_button)
    return main_menu_screen

def tt_menu(screen, font, pos):
    tt_text = "Time Trial"
    tt_screen = Window(GREEN, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, tt_text)
    easy_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Easy', 32, Action.GEN_EASY_MAZE)
    medium_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Medium', 32, Action.GEN_MEDIUM_MAZE)
    hard_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Hard', 32, Action.GEN_HARD_MAZE)
    load_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Load Maze', 32, Action.SET_LOAD_MENU)
    main_menu_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Main Menu', 32, Action.SET_MAIN_MENU)
    tt_screen.add_button(easy_button)
    tt_screen.add_button(medium_button)
    tt_screen.add_button(hard_button)
    tt_screen.add_button(load_button)
    tt_screen.add_button(main_menu_button)
    return tt_screen

def load_menu(screen, font, pos):
    load_text = "Load Maze"
    load_screen = Window(GREEN, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, load_text)
    saved_mazes = get_saved_mazes()
    for name in saved_mazes:
        load_button = Button(GRAY, WHITE, BLACK, 0, 0, 200, BUTTON_HEIGHT, name, 32, Action.LOAD_MAZE)
        load_screen.add_button(load_button)
    main_menu_button = Button(GRAY, WHITE, BLACK, 0, 0, 200, BUTTON_HEIGHT, 'Main Menu', 32, Action.SET_MAIN_MENU)
    load_screen.add_button(main_menu_button)
    return load_screen

def vs_menu(screen, font, pos):
    pass

def victory_menu(screen, font, pos, timer=None):
    victory_text = f"Victory in: {timer.final_time:.2f} seconds!"
    victory_screen = Window(GREEN, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, victory_text)
    retry_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Retry', 32, Action.RETRY)
    save_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Save Maze', 32, Action.SAVE_MAZE)
    main_menu_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Main Menu', 32, Action.SET_MAIN_MENU)
    exit_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Exit', 32, Action.EXIT)
    victory_screen.add_button(retry_button)
    victory_screen.add_button(save_button)
    victory_screen.add_button(main_menu_button)
    victory_screen.add_button(exit_button)
    return victory_screen