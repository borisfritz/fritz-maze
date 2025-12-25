from ui.window import Window
from ui.button import Button
from constants import *

def draw_victory_screen(screen, font, timer, pos):
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
