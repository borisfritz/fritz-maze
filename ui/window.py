import pygame

from constants import BUTTON_SPACING, BORDER_RADIUS, WHITE


class Window:
    def __init__(self, text_color, bg_color, x, y, width, height, text):
        self.text_color = text_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def get_button_clicked(self, pos):
        for button in self.buttons:
            if button.is_over(pos):
                return button.action

    def draw(self, screen, font, pos, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 0, border_radius=BORDER_RADIUS)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height), 0, border_radius=BORDER_RADIUS)
        if self.text == ('' or None):
            print(f"No Window Text for {self}")
        else:
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (50 - text.get_height() / 2)))

        start_y = self.y + 100

        for i in range(len(self.buttons)):
            self.buttons[i].x = self.x + ((self.width / 2) - (self.buttons[i].width / 2))
            if i == 0:
                self.buttons[i].y = start_y
            else:
                self.buttons[i].y = self.buttons[i - 1].y + (self.buttons[i - 1].height + BUTTON_SPACING)
            self.buttons[i].draw(screen, pos, WHITE)
