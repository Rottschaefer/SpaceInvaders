from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor


enemies_row_number = 1
enemies_column_number = 1
menu = Menu()
game = Play()
perfomance_monitor = PerformanceMonitor() 





# loop principal
while True:
    basic_setup.bg.draw()

    match menu.click_button_index:
        case(0):
            game.game()
            if game.game_over:
                menu.click_button_index = -1
                enemies_row_number = 1
                enemies_column_number = 1

                game.go_to_another_fase(enemies_row_number,enemies_column_number) #Reseta a fase

                user_input = input("Qual o seu nome? ")
                game.gravar_pontuacao(user_input)

            elif game.make_fase_harder:
                enemies_row_number += 1
                enemies_column_number += 1
                game.go_to_another_fase(enemies_row_number,enemies_column_number) #Deixa a fase mais dificil

            perfomance_monitor.measure_fps()

        case(2):
            menu.draw_ranking()

        case(-1):
            menu.draw_menu()
            
        



    basic_setup.janela.update()
