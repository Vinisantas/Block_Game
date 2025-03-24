# Configurações do jogo

# Configurações de cores
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Posições do texto de score
SCORE_POS = {
    'Title': (SCREEN_WIDTH / 2, 50),
    'Entername': (SCREEN_WIDTH / 2, 150),
    'AGE': (SCREEN_WIDTH / 2, 250),
    'Name': (SCREEN_WIDTH / 2, 200),
    'Label': (SCREEN_WIDTH / 2, 300),
    'Error': (SCREEN_WIDTH / 2, 350)  # Adicione esta linha para a mensagem de erro
}

# Outras configurações
OPTIONS = ["Start Game", "High Scores", "Exit"]
INITIAL_LIVES = 3
LEVEL_UP_SCORE = 10
MAX_MISSED_BALLOONS = 5
SPECIAL_BALLOON_CHANCE = 10