import pygame

from constants import BORDER_RADIUS


class Button:
    def __init__(self,  button_color, hover_color, text_color, x, y, width, height, text, action):
        self.button_color = button_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action

    def draw(self, screen, pos, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 0, border_radius=BORDER_RADIUS)
        pygame.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height), 0, border_radius=BORDER_RADIUS)
        if self.is_over(pos):
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height), 0, border_radius=BORDER_RADIUS)
        if self.text == ('' or None):
            print(f"No Button Text for {self}")
        else:
            font = pygame.font.Font(None, 32)
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False