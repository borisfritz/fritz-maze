from enum import Enum

# Maze Settings
GRID_SIZE_EASY = 21 #Must be an odd number
GRID_SIZE_MEDIUM = 35
GRID_SIZE_HARD = 53
CELL_SIZE = 20
MARGIN = 200
GENERATION_SPEED = 1
LIBRARY_FILE = "saves/library.json"

# Player Settings
PLAYER_SIZE = CELL_SIZE // 2 - 2
PLAYER_SPEED = 5

# Screen Settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# Button Settings
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_SPACING = 20

# Timer Settings
TIMER_FONT_SIZE = 40
BORDER_PADDING = 30
BORDER_RADIUS = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (40, 40, 40)
GREEN = (0, 255, 0)
DARK_GREEN = (50, 100, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (50, 50, 100)
YELLOW = (255, 255, 0)
WALL_COLOR = (255, 255, 255)
CURRENT_COLOR = (255, 100, 100)

def calculate_margins(grid_size, cell_size):
    maze_width = grid_size * cell_size
    maze_height = grid_size * cell_size
    margin_x = (SCREEN_WIDTH - maze_width) // 2
    margin_y = (SCREEN_HEIGHT - maze_height) // 2
    return margin_x, margin_y

# ENUMS
class GameMode(Enum):
    TIME_TRIAL = "time trial"
    VERSES = "versus"

class GameDifficulty(Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class GameState(Enum):
    MENU = "menu"
    CREATE_MAZE = "create maze"
    GENERATE_MAZE = "generate maze"
    SPAWN_PLAYER = "spawn player"
    PLAYING = "playing"
    FINISHED = "finished"

class MenuState(Enum):
    MAIN = "main menu"
    TT_MENU = "time trial menu"
    VS_MENU = "versus menu"
    LOAD_MENU = "load maze menu"
    VICTORY_MENU = "victory menu"

class Action(Enum):
    SET_MAIN_MENU = "set main menu"
    SET_TT_MENU = "set time trial menu"
    SET_VS_MENU = "set versus menu"
    SET_LOAD_MENU = "set load menu"
    GEN_EASY_MAZE = "generate easy maze"
    GEN_MEDIUM_MAZE = "generate medium maze"
    GEN_HARD_MAZE = "generate hard maze"
    SAVE_MAZE = "save maze"
    LOAD_MAZE = "load maze"
    RETRY = "retry"
    EXIT = "exit"