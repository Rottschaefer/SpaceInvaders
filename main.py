from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
import pygame
import sys
from PPlay.sprite import Sprite
from menu import create_menu, draw_menu

pygame.init()

height = 800
width = 1500

white = (255, 255, 255)
black = (0, 0, 0)
button_color = (111, 111, 111)

janela = Window(width, height)
teclado = Keyboard()

bg = GameImage("./assets/bg.jpeg")

text_paddings = [40, 75, 50, 25]

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
