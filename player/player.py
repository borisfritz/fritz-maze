import pygame

from constants import PLAYER_SIZE, PLAYER_SPEED, PLAYER_COLOR, MARGIN


class Player:
    def __init__(self, start_cell):
        self.x = MARGIN + start_cell.x * start_cell.size + start_cell.size // 2
        self.y = start_cell.y * start_cell.size + start_cell.size // 2
        self.size = PLAYER_SIZE  # radius
        self.speed = PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), self.size)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
