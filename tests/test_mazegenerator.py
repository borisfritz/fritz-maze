import unittest

from maze.mazegenerator import MazeGenerator

class TestMazeGenerator(unittest.TestCase):
    def test_get_cell_0_0(self):
        maze = MazeGenerator(10)
        test_cell = maze.get_cell(0, 0)
        test_cell.visited = True
        self.assertEqual(maze.grid[0][0].visited, True)
        self.assertEqual(maze.grid[1][1].visited, False)

    def test_get_cell_5_2(self):
        maze = MazeGenerator(10)
        test_cell = maze.get_cell(5, 2)
        test_cell.visited = True
        self.assertEqual(maze.grid[4][3].visited, False)
        self.assertEqual(maze.grid[5][2].visited, True)

    def test_get_unvisited_neighbors_1(self):
        maze = MazeGenerator(10)
        test_cell = maze.get_cell(0, 0)
        neighbors = maze.get_unvisited_neighbors(test_cell)
        self.assertEqual(len(neighbors), 2)

    def test_get_unvisited_neighbors_2(self):
        maze = MazeGenerator(10)
        visit_cell = maze.get_cell(5, 7)
        visit_cell.visited = True
        test_cell = maze.get_cell(5, 5)
        neighbors = maze.get_unvisited_neighbors(test_cell)
        self.assertEqual(len(neighbors), 3)

    def test_get_unvisited_neighbors_none(self):
        maze = MazeGenerator(10)
        visit_cell_1 = maze.get_cell(0,2)
        visit_cell_2 = maze.get_cell(2,0)
        visit_cell_1.visited = True
        visit_cell_2.visited = True
        test_cell = maze.get_cell(0, 0)
        neighbors = maze.get_unvisited_neighbors(test_cell)
        self.assertEqual(len(neighbors), 0)

    def test_start_generation(self):
        maze = MazeGenerator(10)
        maze.start_generation()
        self.assertEqual(maze.current, maze.grid[0][0])
        self.assertEqual(maze.generating, True)
        self.assertEqual(maze.generation_complete, False)

if __name__ == '__main__':
    unittest.main()