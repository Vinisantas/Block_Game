import random
import pygame

from BlockGame.Block import Block
from BlockGame.Const import INITIAL_LIVES, LEVEL_UP_SCORE, MAX_MISSED_BLOCKS

class Level:
    def __init__(self, window, score, name='Level 1', game_mode=None):
        self.window = window
        self.score = score
        self.name = name
        self.game_mode = game_mode
        self.running = True
        self.blocks = []
        self.missed_blocks = 0
        self.power = 0
        self.lives = INITIAL_LIVES
        self.level = 1
        self.clock = pygame.time.Clock()
        self.last_power_score = 0  # Adiciona um atributo para armazenar a última pontuação em que o poder foi incrementado
        pygame.mixer.init()
        pygame.mouse.set_visible(True)  # Mostrar o cursor padrão

    def run(self):
        pygame.mixer_music.load('./assets/Level1.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.5)
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.use_power()
            self.update()
            self.draw()
        return "game_over"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_blocks_click(event.pos)

    def use_power(self):
        if self.score % 100 == 0 and self.score != 0 and self.score != self.last_power_score:  # Verifica se a pontuação é um múltiplo de 100 e diferente de 0 e da última pontuação
            self.power += 1
            self.last_power_score = self.score  # Atualiza a última pontuação em que o poder foi incrementado
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.power > 0:
            self.blocks.clear()
            self.score += 20
            self.lives += 1
            self.power -= 1

    def check_blocks_click(self, pos):
        for block in self.blocks:
            if block.rect.collidepoint(pos):
                self.blocks.remove(block)
                pygame.mixer.Sound('./assets/pop.mp3').play()
                if not block.special:
                    self.score += 1
                if block.special:
                    self.score += 9
                    self.lives += 1  # Ganha uma vida ao clicar em um bloco especial
                if self.score % LEVEL_UP_SCORE == 0:
                    self.level += 1
                break

    def update(self):
        if random.randint(1, 100) <= 2 + self.level:  # Aumenta a chance de criar novos blocos com o nível
            self.blocks.append(Block())

        for block in self.blocks:
            block.update()
            if block.rect.y + block.height < 0:
                self.blocks.remove(block)
                self.missed_blocks += 1
                if self.missed_blocks >= MAX_MISSED_BLOCKS:
                    self.lives -= 1
                    self.missed_blocks = 0
                    if self.lives <= 0:
                        pygame.mixer_music.stop()
                        self.running = False

    def draw(self):
        self.window.fill((0, 0, 0))
        for block in self.blocks:
            block.draw(self.window)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        missed_text = font.render(f"Missed: {self.missed_blocks}", True, (255, 255, 255))
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        power_text = font.render(f"Power: {self.power} ", True, (255, 255, 255))

        self.window.blit(score_text, (10, 10))
        self.window.blit(missed_text, (10, 50))
        self.window.blit(level_text, (10, 90))
        self.window.blit(lives_text, (10, 130))
        self.window.blit(power_text, (10, 170))