import datetime
import sys
import pygame

from BlockGame.Const import C_YELLOW, C_WHITE, C_BLACK, SCORE_POS, SCREEN_WIDTH
from BlockGame.DBProxy import DBProxy  

class Score:
    def __init__(self, window):
        self.window = window

    def save(self, game_mode: str, play_score: int):
        db_proxy = DBProxy('DBScore.db')
        name = ''
        age = ''
        error_message = ''
        input_box_color = C_WHITE
        while True:
            self.window.fill(C_BLACK)
            self.score_text(text_size=48, text='SCORE', text_color=C_YELLOW, text_center_pos=SCORE_POS['Title'])
            text = 'Enter Player name (4 characters):'
            age_text = 'Enter Player age (2 characters):'
            self.score_text(text_size=30, text=text, text_color=C_YELLOW, text_center_pos=SCORE_POS['Entername'])
            self.score_text(text_size=25, text=age_text, text_color=C_YELLOW, text_center_pos=SCORE_POS['AGE'])
            self.score_text(text_size=25, text=error_message, text_color=(255, 0, 0), text_center_pos=SCORE_POS['Error'])

            # Draw input boxes
            pygame.draw.rect(self.window, input_box_color, (SCORE_POS['Name'][0] - 100, SCORE_POS['Name'][1] - 20, 200, 40), 2)
            pygame.draw.rect(self.window, input_box_color, (SCORE_POS['Label'][0] - 100, SCORE_POS['Label'][1] - 20, 200, 40), 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4 and len(age) == 2:
                        try:
                            db_proxy.save({'name': name, 'idade': int(age), 'score': play_score, 'date': get_formatted_date()})
                            self.show()
                            return
                        except ValueError:
                            error_message = 'Invalid age. Please enter a valid number.'
                            input_box_color = (255, 0, 0)
                    elif event.key == pygame.K_BACKSPACE:
                        if len(age) > 0:
                            age = age[:-1]
                        elif len(name) > 0:
                            name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
                        elif len(age) < 2:
                            age += event.unicode

            self.score_text(text_size=30, text=name, text_color=C_YELLOW, text_center_pos=SCORE_POS['Name'])
            self.score_text(text_size=30, text=age, text_color=C_YELLOW, text_center_pos=SCORE_POS['Label'])
            pygame.display.flip()

    def show(self):
        db_proxy = DBProxy('DBScore.db')
        score_list = db_proxy.retrieve_top5()
        db_proxy.close()

        self.window.fill(C_BLACK)
        title_text = "High Scores"
        self.score_text(text_size=48, text=title_text, text_color=C_WHITE, text_center_pos=(SCREEN_WIDTH / 2, 50))
        text_info = "Name - Age - Score - Date"
        self.score_text(text_size=20, text=text_info, text_color=C_WHITE, text_center_pos=(SCREEN_WIDTH / 2, 80))

        for i in range(len(score_list)):
            name = score_list[i][1]
            age = score_list[i][2]
            score = score_list[i][3]
            date = score_list[i][4]
            self.score_text(text_size=20, text=f'{name}  - {age} -   {score}     - {date}', text_color=C_YELLOW, text_center_pos=(SCREEN_WIDTH / 2, 100 + i * 30))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"