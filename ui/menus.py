from ui.window import Window
from ui.button import Button
from constants import *
from maze.maze_manager import get_saved_mazes

def _create_window(title, color):
    return Window(color, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, title)

def main_menu(screen, font, pos):
    menu = _create_window("Fritz Maze", WHITE)
    buttons = [
        ('Time Trial', Action.SET_TT_MENU),
        ('VS Mode', Action.SET_VS_MENU),
        ('Exit', Action.EXIT)
    ]
    for text, action in buttons:
        menu.add_button(Button(GRAY, WHITE, BLACK,0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, text, 32, action))
    return menu

def tt_menu(screen, font, pos):
    menu = _create_window("Time Trial", WHITE)
    buttons = [
        ('Easy', Action.GEN_EASY_MAZE),
        ('Medium', Action.GEN_MEDIUM_MAZE),
        ('Hard', Action.GEN_HARD_MAZE),
        ('Load Maze', Action.SET_LOAD_MENU),
        ('Main Menu', Action.SET_MAIN_MENU)
    ]
    for text, action in buttons:
        menu.add_button(Button(GRAY, WHITE, BLACK,0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, text, 32, action))
    return menu

def load_menu(screen, font, pos):
    menu = _create_window("Load Maze", WHITE)
    for name in get_saved_mazes():
        menu.add_button(Button(GRAY, WHITE, BLACK, 0, 0, 200, BUTTON_HEIGHT, name, 32, Action.LOAD_MAZE))
    menu.add_button(Button(GRAY, WHITE, BLACK, 0, 0, 200, BUTTON_HEIGHT, 'Main Menu', 32, Action.SET_MAIN_MENU))
    return menu

def vs_menu(screen, font, pos):
    menu = _create_window("Versus Mode", WHITE)
    buttons = [
        ('Easy AI', Action.GEN_EASY_MAZE),
        ('Medium AI', Action.GEN_MEDIUM_MAZE),
        ('Hard AI', Action.GEN_HARD_MAZE),
        ('Main Menu', Action.SET_MAIN_MENU)
    ]
    for text, action in buttons:
        menu.add_button(Button(GRAY, WHITE, BLACK,0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, text, 32, action))
    return menu

def victory_menu(screen, font, pos, timer=None):
    title = f"Victory in: {timer.final_time:.2f}s!" if timer else "Victory!"
    menu = _create_window(title, GREEN)
    buttons = [
        ('Retry', Action.RETRY),
        ('Save Maze', Action.SAVE_MAZE),
        ('Main Menu', Action.SET_MAIN_MENU),
        ('Exit', Action.EXIT)
    ]
    for text, action in buttons:
        menu.add_button(Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, text, 32, action))
    return menu