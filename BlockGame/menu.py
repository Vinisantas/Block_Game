import sys
import pygame
from BlockGame.Const import C_WHITE, C_YELLOW, C_BLACK, OPTIONS, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont(None, 48)
        self.options = OPTIONS
        self.selected_option = 0

    def run(self):
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.fill(C_BLACK)
            self.draw_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer_music.stop()
                        return self.options[self.selected_option]
                        

    def draw_menu(self):
        title_text = self.font.render("BALLOON GAME", True, C_YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        self.window.blit(title_text, title_rect)

        for i, option in enumerate(self.options):
            color = C_YELLOW if i == self.selected_option else C_WHITE
            option_text = self.font.render(option, True, color)
            option_rect = option_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + i * 50))
            self.window.blit(option_text, option_rect)