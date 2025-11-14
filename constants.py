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

# Colors
BLACK = (0, 0, 0)
WALL_COLOR = (255, 255, 255)
PATH_COLOR = (40, 40, 40)
CURRENT_COLOR = (255, 100, 100)
START_COLOR = (50, 100, 50)
END_COLOR = (50, 50, 100)
PLAYER_COLOR = (255, 0, 0)

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
    GENERATE_MAZE = "generate maze"
    SPAWN_PLAYER = "spawn player"
    PLAYING = "playing"
    FINISHED = "finished"