
from button import create_button
from utils import get_text_dimensions
import constants
from PPlay.keyboard import Keyboard

def create_menu(janela, mouse, menu_options):

    buttons = create_button(menu_options)

    for i in range(len(buttons)):

        
            
        buttons[i].draw()
        [text_width, text_height] = get_text_dimensions(menu_options[i], constants.MENU_FONT_SIZE)

        #Por algum motivo a palavra DIFICULDADE estava ficando mal centralizada, então fiz um ajuste só pra que ela ficasse centralizada
        if(menu_options[i] == "DIFICULDADE"):
            text_x = buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 - 25
        else:
            text_x = buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 -15
        text_y = constants.BUTTON_MARGIN_TOP + i * constants.BUTTON_MARGIN + constants.BUTTON_HEIGHT/2 - text_height/2 - 5
        janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.TEXT_COLOR)

        if mouse.is_over_object(buttons[i]):
            text_color = (255, 0, 0)

            janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.HOVER_TEXT_COLOR)

            if mouse.is_button_pressed(1):
                return i

        
def ranking(janela, mouse, menu_options):
    while True:
        create_menu(janela, mouse, menu_options)

def play(janela, mouse):
    while True:
                if Keyboard().key_pressed("ESC"):
                    break
                janela.update()

def difficulty(janela, mouse, menu_options):
    return create_menu(janela, mouse, menu_options)

    # if output == 3:
    #     menu_options[3] = 0



    




