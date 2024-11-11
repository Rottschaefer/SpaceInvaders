from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
import pygame
from button import draw_button

def create_menu(janela):

    button_width = 300
    button_heigth = 100 
    button_color = (111, 111, 111)

    buttons_margin = 150
    buttons_margin_top = 125


    bg = GameImage("./assets/bg.jpeg")
    menu_options = ["JOGAR", "DIFICULDADE", "RANKING", "SAIR"]
    text_color = (255, 255, 255)

    button = {
            "text",
            "x",
            "y",
            "width",
            "height",
            "color",
            "text_color"
        }
    buttons = len(menu_options)*[button]

    for i, option in enumerate(menu_options):
        button = {
            "text": option,
            "x": (janela.width - button_width) / 2,
            "y": buttons_margin_top + i * buttons_margin,
            "width": button_width,
            "height": button_heigth,
            "color": button_color,
            "text_color": text_color
        }

        buttons[i] = button

    return bg, buttons

def draw_menu(bg, buttons):

    border_radius = 10
    bg.draw()
    for button in buttons:
        draw_button(pygame.display.get_surface(), button["text"], button["x"], button["y"], button["width"], button["height"], button["color"], button["text_color"], border_radius)