import pygame

from constants import BORDER_RADIUS


class Button:
    def __init__(self,  button_color, hover_color, text_color, x, y, width, height, text, size, action):
        self.button_color = button_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.size = size
        self.action = action

    def draw(self, screen, pos, outline=None):
        color = self.hover_color if self.is_over(pos) else self.button_color
        self._draw_background(screen, color, outline)
        if not self.text:
            print(f"No Button Text for {self}")
        else:
            self._draw_text(screen)

    def _draw_background(self, screen, color, outline):
        if outline:
            outline_rect = self.rect.inflate(10, 10)
            pygame.draw.rect(screen, outline, outline_rect, border_radius=BORDER_RADIUS)
        pygame.draw.rect(screen, color, self.rect, border_radius=BORDER_RADIUS)

    def _draw_text(self, screen):
        font = pygame.font.Font(None, self.size)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)