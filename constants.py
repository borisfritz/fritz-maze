from enum import Enum

# Maze Settings
GRID_SIZE_EASY = 21 #Must be an odd number
GRID_SIZE_MEDIUM = 35
GRID_SIZE_HARD = 53
CELL_SIZE = 20
MARGIN = 200
GENERATION_SPEED = 1

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
class GameScreen(Enum):
    MAIN = "main menu"
    TIME_TRIAL_MENU = "time trial menu"
    VERSES_MENU = "versus menu"
    GAME = "game"

class GameMode(Enum):
    TIME_TRIAL = "time trial"
    VERSES = "versus"

class GameDifficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class GameState(Enum):
    MENU = "menu"
    GENERATE_MAZE = "generate maze"
    SPAWN_PLAYER = "spawn player"
    PLAYING = "playing"
    FINISHED = "finished"

class MenuState(Enum):
    MAIN = "main menu"
    TT_MENU = "time trial menu"
    VS_MENU = "versus menu"
    VICTORY_MENU = "victory menu"

class Action(Enum):
    MAIN_MENU = "Main Menu"
    TIME_TRIAL_MENU = "Time Trial Menu"
    VS_MENU = "Versus Menu"
    GEN_EASY_MAZE = "Generate Easy Maze"
    GEN_MEDIUM_MAZE = "Generate Medium Maze"
    GEN_HARD_MAZE = "Generate Hard Maze"
    RETRY = "retry"
    EXIT = "exit"