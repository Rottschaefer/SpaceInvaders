import pygame
import constants
from PPlay.gameimage import GameImage


# Define a fonte
font = pygame.font.Font(None, 36)

def draw_button(screen, text, x, y, width, height, color, text_color, border_radius):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=border_radius)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

def create_button(menu_options):

    buttons = len(menu_options)*[None]

    #Criação de uma GameImage para cada botão em menu_optionsseguindo os valores das constantes definidas em constants.py
    for index in range(len(menu_options)):

        button = GameImage("./assets/button.png")
        button.set_position(constants.WINDOW_WIDTH/2 - constants.BUTTON_WIDTH/2, constants.BUTTON_MARGIN_TOP + index * constants.BUTTON_MARGIN)

        buttons[index] = button

    return buttons
