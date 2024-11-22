from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite
import constants

teclado = Keyboard()

def play(janela, bg):

    nave = Sprite("./assets/nave.png")
    nave.x = constants.WINDOW_WIDTH/2 - constants.NAVE_WIDTH/2
    nave.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH - 10

    nave_speed = 300


    #Loop vazio que só vai sair quando o usuário pressionar a tecla ESC
    while True:

        bg.draw()

        print(teclado.show_key_pressed())

        pode_mover = nave.x > 0 or (nave.x <= 0 and teclado.key_pressed("RIGTH")) or (nave.x >= constants.WINDOW_WIDTH- constants.NAVE_WIDTH and teclado.key_pressed("LEFT"))

        if(pode_mover):
            nave.move_key_x(nave_speed*janela.delta_time())

        nave.draw()
        
        if Keyboard().key_pressed("ESC"):
            break
        janela.update()
