from PPlay.window import *
from PPlay.gameimage import *
from button import criar_botoes
from menu import create_menu, handle_menu
import constants

#considerações iniciais
janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
bg = GameImage("./assets/bg.jpeg")
mouse = janela.get_mouse()
teclado = janela.get_keyboard()


# loop principal
while True:
    bg.draw()

    handle_menu(janela, bg)

    janela.update()
