from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play


menu = Menu()
game = Play()



# loop principal
while True:
    basic_setup.bg.draw()

    match menu.click_button_index:
        case(0):
            game.go_to_game()
        case(-1):
            menu.handle_menu()


    basic_setup.janela.update()
