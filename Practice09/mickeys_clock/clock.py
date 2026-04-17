import pygame
import datetime

class MickeyClock:
    def __init__(self):
        self.hand = pygame.image.load("images/mickey_hand.png")
        self.hand = pygame.transform.scale(self.hand, (150, 150))

    def draw(self, screen):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        # угол (360 градусов / 60)
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        sec_hand = pygame.transform.rotate(self.hand, sec_angle)
        min_hand = pygame.transform.rotate(self.hand, min_angle)

        rect = sec_hand.get_rect(center=(400, 300))
        rect2 = min_hand.get_rect(center=(400, 300))

        screen.blit(min_hand, rect2)
        screen.blit(sec_hand, rect)