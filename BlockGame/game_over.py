import pygame
from BlockGame.Const import  C_YELLOW, C_BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from BlockGame.Score import Score

class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score

    def game_over_text(self, text_size, text, text_color, text_center_pos):
        font = pygame.font.SysFont(None, text_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(text_surface, text_rect)

    def show(self):
        pygame.mixer_music.load("./assets/GameOver.mp3")
        self.window.fill(C_BLACK)
        self.game_over_text(
            text_size=100,
            text="GAME OVER",
            text_color=C_YELLOW,
            text_center_pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        )
        pygame.display.flip()
        pygame.time.wait(3000)  # Espera 3 segundos antes de fechar

        # Espera até que o usuário pressione uma tecla ou feche a janela
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    score_screen = Score(self.window)
                    score_screen.save("game_over", self.score)  # Passa os argumentos corretos
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # Fecha o jogo
