from maze.cell import Cell

class MazeGenerator:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[Cell(x, y) for y in range(self.grid_size)] for x in range(self.grid_size)]

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)