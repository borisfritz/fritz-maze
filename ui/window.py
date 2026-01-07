import pygame
from constants import BUTTON_SPACING, BORDER_RADIUS, WHITE, BUTTON_HEIGHT


class Window:
    def __init__(self, text_color, bg_color, x, y, width, height, text):
        self.text_color = text_color
        self.bg_color = bg_color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.buttons = []
        self.current_page = 0
        self.max_per_page = (self.rect.height -  150) // (BUTTON_HEIGHT + BUTTON_SPACING)

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
        self._draw_background(screen, outline)
        self._draw_header(screen, font)

        if not self.buttons:
            return

        start_idx = self.current_page * self.max_per_page
        end_idx = start_idx + self.max_per_page
        page_buttons = self.buttons[start_idx:end_idx]

        start_y = self.rect.y + 100
        for i, button in enumerate(page_buttons):
            button.rect.centerx =  self.rect.centerx
            button.rect.y = start_y + (i * (BUTTON_HEIGHT + BUTTON_SPACING))
            button.draw(screen, pos, WHITE)

        self._draw_page_indicators(screen)

    def _draw_background(self,screen, outline):
        if outline:
            pygame.draw.rect(screen, outline, (self.rect.x - 5, self.rect.y - 5, self.rect.width + 10, self.rect.height + 10), 0, border_radius=BORDER_RADIUS)
        pygame.draw.rect(screen, self.bg_color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 0, border_radius=BORDER_RADIUS)

    def _draw_header(self, screen, font):
        if not self.text:
            print(f"No Window Text for {self}")
            return
        text_surf = font.render(self.text, True, self.text_color)
        text_x = self.rect.x + (self.rect.width - text_surf.get_width()) / 2
        text_y = self.rect.y + (50 - text_surf.get_height() / 2)
        screen.blit(text_surf, (text_x, text_y))

    def _draw_page_indicators(self, screen):
        total_pages = (len(self.buttons) - 1) // self.max_per_page + 1
        if total_pages <= 1:
            return
        page_font = pygame.font.Font(None, 28)
        messages = [f"Page {self.current_page + 1}/{total_pages}", "Scroll to change page"]
        for i, msg in enumerate(messages):
            surf = page_font.render(msg, True, WHITE)
            y_offset = 50 if i == 0 else 25
            rect = surf.get_rect(centerx=self.rect.centerx, bottom=self.rect.bottom - y_offset)
            screen.blit(surf, rect)