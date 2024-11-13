from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import pygame
import constants
from menu import create_menu, play, handle_menu

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

while True:

    bg.draw()

    handle_menu(janela, teclado, mouse, bg)

    if teclado.key_pressed("ESC"):
        janela.close()

