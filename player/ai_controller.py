import random
from constants import GameDifficulty

class AIController:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.path_stack = []
        self.visited = set()
        self.target_cell = None
        self.decision_cooldown = 0
        self.max_cooldown = self._set_difficulty_settings()

    def get_move(self, ai_player, maze):
        curr_cell = ai_player.get_current_cell(maze)
        if curr_cell not in self.visited:
            self.visited.add(curr_cell)
            self.path_stack.append(curr_cell)

        if not self.target_cell or self._is_at_target(ai_player, maze, self.target_cell):
            if self.decision_cooldown > 0:
                self.decision_cooldown -= 1
                return (0, 0)
            self.decision_cooldown = self.max_cooldown
            self.target_cell = self._choose_next_cell(curr_cell, maze)
        return self._calculate_velocity(ai_player, maze, self.target_cell)

    def _set_difficulty_settings(self):
        from constants import GameDifficulty
        match self.difficulty:
            case GameDifficulty.EASY:
                return 2
            case GameDifficulty.MEDIUM:
                return 1
            case GameDifficulty.HARD:
                return 0
        return 0

    def _choose_next_cell(self, curr_cell, maze):
        options = [n for n in curr_cell.neighbors if n not in self.visited]
        if options:
            options.sort(key=lambda c: abs(c.x - maze.end_cell.x) + abs(c.y - maze.end_cell.y))
            mistake_chance = 0.4 if self.difficulty == GameDifficulty.EASY else 0.1
            if random.random() < mistake_chance:
                next_step = random.choice(options)
            else:
                next_step = options[0]
            return next_step
        elif self.path_stack:
            self.path_stack.pop()
            if self.path_stack:
                return self.path_stack[-1]
        return curr_cell

    def _is_at_target(self, player, maze, target):
        target_x = target.x * maze.cell_size + maze.cell_size // 2 +  maze.margin_x
        target_y = target.y * maze.cell_size + maze.cell_size // 2 +  maze.margin_y
        return abs(player.x - target_x) < 2 and abs(player.y - target_y) < 2

    def _calculate_velocity(self, player, maze, target):
        target_x = target.x * maze.cell_size + maze.cell_size // 2 +  maze.margin_x
        target_y = target.y * maze.cell_size + maze.cell_size // 2 +  maze.margin_y
        dx, dy = 0, 0
        if player.x < target_x:
            dx = player.speed
        elif player.x > target_x:
            dx = -player.speed
        if player.y < target_y:
            dy = player.speed
        elif player.y > target_y:
            dy = -player.speed
        return (dx, dy)