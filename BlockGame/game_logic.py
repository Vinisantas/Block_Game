
import pygame

from BlockGame.Const import OPTIONS, SCREEN_HEIGHT, SCREEN_WIDTH
from BlockGame.Level import Level
from BlockGame.menu import Menu
from BlockGame.game_over import GameOver
from BlockGame.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [OPTIONS[0]]:
                player_score = 0
                level = Level(self.window, player_score, name='Level 1', game_mode=menu_return)
                level_return = level.run()
                if level_return == 'game_over':
                    game_over = GameOver(self.window, level.score)  # Passa o score para GameOver
                    game_over.show()
            elif menu_return in [OPTIONS[1]]:
                score_screen = Score(self.window)
                score_screen.show()
            elif menu_return in [OPTIONS[2]]:
                pygame.quit()
                quit()





