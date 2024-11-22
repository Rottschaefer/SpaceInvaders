
from button import criar_botoes
from utils import get_text_dimensions
from play import play
import constants
import pygame
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

mouse = Mouse()

def create_menu(janela, mouse, menu_options):

    buttons = criar_botoes(menu_options)

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

            janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.HOVER_TEXT_COLOR)

            if mouse.is_button_pressed(1):
                return i

def handle_menu(janela, bg):

    while True:

        condicao = create_menu(janela, mouse, ["START", "DIFICULDADE", "RANKING", "SAIR", "FACIL", "MEDIO", "DIFICIL"])

        if condicao == 0:
            bg.draw()
            play(janela, bg)

        elif condicao == 1:
            while True:

                option = ["VOLTAR", "FÁCIL", "MÉDIO", "DIFÍCIL"]

                menu_choice = create_menu(janela, mouse, option)

                if (menu_choice == 0):
                #É preciso dar um delay aqui pois quando o usuário clica em voltar, o mouse ainda está sobre o botão e ele acaba clicando no botão do menu que é exibido logo em seguida
                    pygame.time.wait(200)
                    break
               
                janela.update()

        elif condicao == 3:
            janela.close()

        janela.update()
        
# def ranking(janela, mouse, menu_options):
#     while True:
#         create_menu(janela, mouse, menu_options)


# def difficulty(janela, mouse, menu_options):
#     return create_menu(janela, mouse, menu_options)

#     # if output == 3:
#     #     menu_options[3] = 0



    




