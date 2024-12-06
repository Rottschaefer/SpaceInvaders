from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from button import criar_botoes
from menu import handle_menu
import constants

#considerações iniciais
# janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
# bg = GameImage("./assets/bg.jpeg")
# mouse = janela.get_mouse()
# teclado = janela.get_keyboard()


last_time = 0


# loop principal
while True:
    basic_setup.bg.draw()

    print(basic_setup.janela)

    handle_menu(basic_setup.janela, basic_setup.bg)


    basic_setup.janela.update()
