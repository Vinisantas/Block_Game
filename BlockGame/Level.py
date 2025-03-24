import random
import pygame

from BlockGame.Const import INITIAL_LIVES, LEVEL_UP_SCORE, MAX_MISSED_BALLOONS
from BlockGame.Block import Balloon


class Level:
    def __init__(self, window, score, name='Level 1', game_mode=None):
        self.window = window
        self.score = score
        self.name = name
        self.game_mode = game_mode
        self.running = True
        self.balloons = []
        self.missed_balloons = 0
        self.lives = INITIAL_LIVES
        self.level = 1
        self.clock = pygame.time.Clock()
        pygame.mixer.init()

    def run(self):
        pygame.mixer_music.load('./assets/Level1.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.5)
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        return "game_over"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_balloon_click(event.pos)

    def check_balloon_click(self, pos):
        for balloon in self.balloons:
            if balloon.rect.collidepoint(pos):
                self.balloons.remove(balloon)
                pygame.mixer.Sound('./assets/pop.mp3').play()
                if not balloon.special:
                    self.score += 1
                if balloon.special:
                    self.score += 9
                    self.lives += 1  # Ganha uma vida ao clicar em um balão especial
                if self.score % LEVEL_UP_SCORE == 0:
                    self.level += 1
                    #if self.score == 50:


                break
                

    def update(self):
        if random.randint(1, 100) <= 2 + self.level:  # Aumenta a chance de criar novos balões com o nível
            self.balloons.append(Balloon())

        for balloon in self.balloons:
            balloon.update()
            if balloon.rect.y + balloon.height < 0:
                self.balloons.remove(balloon)
                self.missed_balloons += 1
                if self.missed_balloons >= MAX_MISSED_BALLOONS:
                    self.lives -= 1
                    self.missed_balloons = 0
                    if self.lives <= 0:
                        pygame.mixer_music.stop()
                        self.running = False

    def draw(self):
        self.window.fill((0, 0, 0))
        for balloon in self.balloons:
            balloon.draw(self.window)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        missed_text = font.render(f"Missed: {self.missed_balloons}", True, (255, 255, 255))
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))
        self.window.blit(missed_text, (10, 50))
        self.window.blit(level_text, (10, 90))
        self.window.blit(lives_text, (10, 130))