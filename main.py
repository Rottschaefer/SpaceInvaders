from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor
import pygame
from constants import *
from EnemyTest import enemies



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

        case(1):
            pygame.time.delay(100)
            menu.click_button_index = -2

            

            while True:

                
                basic_setup.bg.draw()
                menu.draw_difficulty_menu()



                match (menu.click_button_index):
                    case(0):
                    
                        enemy_speed = 150
                        enemies.__init__(1,1, enemy_speed)
                        menu.click_button_index = -1
                        pygame.time.delay(100)
                        
                        
                        break
                    case(1):

                        enemy_speed = 200
                        enemies.__init__(3,3,enemy_speed)

                            
                        
                        menu.click_button_index = -1
                        pygame.time.delay(100)
                        

                        break
                    case(2):
                    
                        enemy_speed = 250
                        enemies.__init__(5,5, enemy_speed)
                        menu.click_button_index = -1
                        pygame.time.delay(100)
                        

                        break
                    case(3):
                        menu.click_button_index = -1
                        pygame.time.delay(100)
                        
                        break


                basic_setup.janela.update()
               
        case(2):
            menu.draw_ranking()
        case(3):
            basic_setup.janela.close()

        case(-1):
            menu.draw_menu()
            
        



    basic_setup.janela.update()
