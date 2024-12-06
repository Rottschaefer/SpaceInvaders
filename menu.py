
# from button import criar_botoes
# from utils import get_text_dimensions
# from play import play
import constants
import pygame
from PPlay.mouse import Mouse
from performance import PerformanceMonitor
from MenuClass import Menu
from BaseClass import basic_setup


mouse = Mouse()

performance_monitor = PerformanceMonitor()

menuClass = Menu()


# def create_menu(janela, mouse, menu_options, bg):


#     menuClass.create_buttons()

#     for i in range(len(menuClass.current_buttons)):

        
            
#         menuClass.current_buttons[i].draw()
#         [text_width, text_height] = get_text_dimensions(menu_options[i], constants.MENU_FONT_SIZE)

#         #Por algum motivo a palavra DIFICULDADE estava ficando mal centralizada, então fiz um ajuste só pra que ela ficasse centralizada
#         if(menu_options[i] == "DIFICULDADE"):
#             text_x = menuClass.current_buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 - 25
#         else:
#             text_x = menuClass.current_buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 -15
#         text_y = constants.BUTTON_MARGIN_TOP + i * constants.BUTTON_MARGIN + constants.BUTTON_HEIGHT/2 - text_height/2 - 5
#         janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.TEXT_COLOR)

#         if mouse.is_over_object(menuClass.current_buttons[i]):

#             janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.HOVER_TEXT_COLOR)

#             if mouse.is_button_pressed(1):
#                 return i
            

def handle_menu(janela, bg):

    while True:

        basic_setup.bg.draw()

        performance_monitor.measure_fps(janela)

        # condicao = create_menu(janela, mouse, ["START", "DIFICULDADE", "RANKING", "SAIR"], bg)
        menuClass.create_menu()

        basic_setup.janela.update()

        # handle_game_flow(janela, bg, menuClass.)

        

# def handle_game_flow(janela, bg, condicao):
#         if condicao == 0:
#             # bg.draw()
#             play(janela, bg)

#         elif condicao == 1:
#             difficulty(janela, mouse)

#         elif condicao == 3:
#             janela.close()

#         janela.update()


# def difficulty(janela, mouse):

#     menu_options = ["VOLTAR", "FÁCIL", "MÉDIO", "DIFÍCIL"]

#     while True:

#         clicked = create_menu(janela, mouse, menu_options)

#         if (clicked == 0):
#                 #É preciso dar um delay aqui pois quando o usuário clica em voltar, o mouse ainda está sobre o botão e ele acaba clicando no botão do menu que é exibido logo em seguida
#                 pygame.time.wait(200)
#                 break


#         if(clicked):

#             #alteracao das constantes de velocidade pra deixar o jogo mais dificil
#             constants.shot_delay =0.5*clicked
#             constants.nave_speed = 500 - 100*clicked
        
#         janela.update()




    




