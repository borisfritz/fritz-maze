from ui.window import Window
from ui.button import Button
from constants import *

def draw_main_menu(screen, font, pos):
    main_menu_text = "Fritz Maze Game!"
    main_menu_screen = Window(WHITE, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, main_menu_text)
    tt_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Time Trial', Action.TIME_TRIAL_MENU)
    vs_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Versus', Action.VS_MENU)
    exit_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Exit', Action.EXIT)
    main_menu_screen.add_button(tt_button)
    main_menu_screen.add_button(vs_button)
    main_menu_screen.add_button(exit_button)
    main_menu_screen.draw(screen, font, pos, WHITE)
    return main_menu_screen

def draw_tt_menu(screen, font, pos):
    tt_text = "Time Trial"
    tt_screen = Window(GREEN, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, tt_text)
    easy_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Easy', Action.GEN_EASY_MAZE)
    medium_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Medium', Action.GEN_MEDIUM_MAZE)
    hard_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Hard', Action.GEN_HARD_MAZE)
    main_menu_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Main Menu', Action.MAIN_MENU)
    tt_screen.add_button(easy_button)
    tt_screen.add_button(medium_button)
    tt_screen.add_button(hard_button)
    tt_screen.add_button(main_menu_button)
    tt_screen.draw(screen, font, pos, WHITE)
    return tt_screen

def draw_vs_menu(screen, font, pos):
    pass

def draw_victory_menu(screen, font, pos, timer=None):
    victory_text = f"Victory in: {timer.final_time} seconds!"
    victory_screen = Window(GREEN, BLACK, (SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250, 500, 500, victory_text)
    main_menu_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Main Menu', Action.MAIN_MENU)
    retry_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Retry', Action.RETRY)
    exit_button = Button(GRAY, WHITE, BLACK, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, 'Exit', Action.EXIT)
    victory_screen.add_button(main_menu_button)
    victory_screen.add_button(retry_button)
    victory_screen.add_button(exit_button)
    victory_screen.draw(screen, font, pos, WHITE)
    return victory_screen