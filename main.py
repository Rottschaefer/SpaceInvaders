from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from button import criar_botoes
import constants

#considerações iniciais
# janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
# bg = GameImage("./assets/bg.jpeg")
# mouse = janela.get_mouse()
# teclado = janela.get_keyboard()

menu = Menu()

# loop principal
while True:
    basic_setup.bg.draw()

    menu.handle_menu()

    basic_setup.janela.update()
