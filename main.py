from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import pygame
import constants
from menu import create_menu, play, difficulty

pygame.init()

janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
teclado = Keyboard()
mouse = Mouse()

bg = GameImage("./assets/bg.jpeg")

# Define os estados do jogo
MENU = 0
PLAYING = 1
DIFFICULTY = 2
RANKING = 3
EXIT = 4

# Estado inicial
state = MENU

while state != EXIT:

    bg.draw()

    if state == MENU:
        menu_choice = create_menu(janela, mouse, ["JOGAR", "DIFICULDADE", "RANKING", "SAIR"])
        match(menu_choice):
            case 0:
                state = PLAYING
            case 1:
                state = DIFFICULTY
            case 2:
                state = RANKING
            case 3:
                state = EXIT

    elif state == PLAYING:
        play(janela, mouse)
        state = MENU  # Retorna ao menu após jogar

    elif state == DIFFICULTY:
        option = ["FÁCIL", "MÉDIO", "DIFÍCIL", "VOLTAR"]
        difficulty_choice = difficulty(janela, mouse, option)

        if difficulty_choice == 3:  # Se a opção "VOLTAR" for selecionada
            state = MENU

        if option[3] == 0:
            state = MENU
        # state = MENU  # Retorna ao menu após escolher a dificuldade

    elif state == RANKING:
        # Adicione a lógica do ranking aqui
        state = MENU  # Retorna ao menu após visualizar o ranking

    janela.update()

    if teclado.key_pressed("ESC"):
        state = EXIT

janela.close()
