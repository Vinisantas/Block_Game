# Block Game

Block Game é um jogo simples desenvolvido em Python usando a biblioteca Pygame. O objetivo do jogo é clicar nos blocos que aparecem na tela para ganhar pontos e evitar que eles saiam da tela. O jogo também possui blocos especiais que concedem pontos extras e vidas adicionais.

## Funcionalidades

- Clique nos blocos para ganhar pontos.
- Blocos especiais que concedem pontos extras e vidas adicionais.
- Sistema de níveis que aumenta a dificuldade conforme o jogador avança.
- Sistema de poder que permite limpar todos os blocos da tela e ganhar pontos extras.

## Requisitos

- Python 3.x
- Pygame 2.6.1

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/block-game.git
    cd block-game
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como Jogar

1. Execute o jogo:

    ```bash
    python main.py
    ```

2. Use o mouse para clicar nos blocos que aparecem na tela.
3. Pressione a barra de espaço para usar o poder quando disponível.

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicia o jogo.
- `BlockGame/Block.py`: Define a classe `Block` que representa os blocos no jogo.
- `BlockGame/Const.py`: Contém constantes usadas no jogo.
- `BlockGame/Level.py`: Define a classe `Level` que gerencia a lógica do jogo.
- `BlockGame/game_logic.py`: Contém a lógica principal do jogo.
- `BlockGame/menu.py`: Define a classe `Menu` que gerencia o menu do jogo.
- `BlockGame/game_over.py`: Define a classe `GameOver` que gerencia a tela de game over.
- `BlockGame/Score.py`: Define a classe `Score` que gerencia a pontuação do jogo.
- `BlockGame/DBProxy.py`: Define a classe `DBProxy` que gerencia a persistência dos dados do jogo.

## Compilação

Para compilar o jogo em um executável, você pode usar o PyInstaller. Um arquivo de especificação (`main.spec`) já está incluído no projeto.

1. Instale o PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2. Compile o jogo:

    ```bash
    pyinstaller main.spec
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
