from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
import pygame
from menu import create_menu, draw_menu

pygame.init()

height = 800
width = 1500

janela = Window(width, height)
teclado = Keyboard()

bg = GameImage("./assets/bg.jpeg")


# Loop principal
while True:
    bg.draw()

    [bg, buttons] = create_menu(janela)
    draw_menu(bg, buttons)
    

    if teclado.key_pressed("ENTER"):
        break

    if teclado.key_pressed("ESC"):
        janela.close()
        break

    janela.update()
