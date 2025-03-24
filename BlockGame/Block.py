import pygame
import random

from BlockGame.Const import SCREEN_HEIGHT, SCREEN_WIDTH, SPECIAL_BALLOON_CHANCE

class Balloon:
    def __init__(self):
        self.width = random.randint(30, 70)
        self.height = random.randint(40, 90)
        self.image = pygame.Surface((self.width, self.height))
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.rect.y = SCREEN_HEIGHT
        self.speed = random.uniform(1.0, 3.0)
        self.horizontal_speed = random.uniform(-1.0, 1.0)
        self.special = random.randint(1, 100) <= SPECIAL_BALLOON_CHANCE
        

    def update(self):
        self.rect.y -= self.speed
        self.rect.x += self.horizontal_speed
        if self.rect.x < 0 or self.rect.x + self.width > SCREEN_WIDTH:
            self.horizontal_speed = -self.horizontal_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)