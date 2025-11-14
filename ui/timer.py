import pygame

class Timer:
    def __init__(self, time):
        self.start_time = time
        self.final_time = 0
        self.is_stopped = False
        self.font = pygame.font.Font(None, 36)

    def stop_time(self):
        self.is_stopped = True
        self.final_time = (pygame.time.get_ticks() - self.start_time) / 1000

    def draw(self, screen):
        if not self.is_stopped:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
            timer_text = self.font.render(f"Time: {elapsed_time:.2f}", True, (255, 255, 255))
            screen.blit(timer_text, (20, 20))
        elif self.is_stopped:
            timer_text = self.font.render(f"Time: {self.final_time:.2f}", True, (255, 255, 255))
            screen.blit(timer_text, (20, 20))

