import pygame

from constants import BUTTON_SPACING, BORDER_RADIUS, WHITE, BUTTON_HEIGHT


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
        self.current_page = 0
        self.max_per_page = (self.height -  150) // (BUTTON_HEIGHT + BUTTON_SPACING)

    def add_button(self, button):
        self.buttons.append(button)

    def get_button_clicked(self, pos):
        start = self.current_page * self.max_per_page
        end = start + self.max_per_page
        for button in self.buttons[start:end]:
            if button.is_over(pos):
                return button
        return None

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
        if self.buttons:
            start_idx = self.current_page * self.max_per_page
            end_idx = start_idx + self.max_per_page
            page_buttons = self.buttons[start_idx:end_idx]

            for i, button in enumerate(page_buttons):
                button.x = self.x + ((self.width / 2 ) - (button.width / 2))
                button.y = start_y + (i * (BUTTON_HEIGHT + BUTTON_SPACING))
                button.draw(screen, pos, WHITE)

            total_pages = (len(self.buttons) - 1) // self.max_per_page + 1
            if total_pages > 1:
                page_font = pygame.font.Font(None, 28)
                page_text = page_font.render(f"Page {self.current_page + 1}/{total_pages}", True, WHITE)
                scroll_text = page_font.render("Scroll to change page", True, WHITE)
                screen.blit(page_text, (self.x + (self.width / 2 - page_text.get_width() / 2), self.y + self.height - 50))
                screen.blit(scroll_text, (self.x + (self.width / 2 - scroll_text.get_width() / 2), self.y + self.height - 25))