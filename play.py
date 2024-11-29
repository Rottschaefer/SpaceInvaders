from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite
from bullet import create_bullet
import constants
from utils import set_scale
from performance import PerformanceMonitor
from enemy import Enemy


teclado = Keyboard()
performance_monitor = PerformanceMonitor()

def play(janela, bg):
    nave = Sprite("./assets/nave.png")
    set_scale("./assets/nave.png", constants.NAVE_WIDTH, constants.NAVE_HEIGTH)
    set_scale("./assets/bullet.png", 10, 40)

    enemies = Enemy()


    nave.x = constants.WINDOW_WIDTH / 2 - constants.NAVE_WIDTH / 2
    nave.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH - 10

    bullets = []  # Lista para armazenar os tiros

    last_shot_time = 0

    while True:

        performance_monitor.measure_fps(janela) #monitoramento do FPS

        bg.draw()

        enemies.draw_enemies()
        enemies.move_enemies(janela)

        last_shot_time += janela.delta_time() # Contador de tempo para respeitar o delay do tiro

        # Movimento da nave
        pode_mover = (nave.x > 0 and teclado.key_pressed("LEFT")) or (nave.x < constants.WINDOW_WIDTH - constants.NAVE_WIDTH and teclado.key_pressed("RIGHT"))
        if pode_mover:
            nave.move_key_x(constants.nave_speed * janela.delta_time())

        # Disparo de tiros
        if teclado.key_pressed("SPACE"):
            if(last_shot_time > constants.shot_delay):
                last_shot_time = 0
                bullet = create_bullet(nave.x + constants.NAVE_WIDTH / 2 - 5, nave.y)

                bullets.append(bullet)

            


        for bullet in bullets:
            if(bullet.y < 0):
                bullets.remove(bullet) #remocao da bala caso ela saia da tela
            
            bullet.y -= constants.BULLET_SPEED * janela.delta_time() #movimentacao da bala
            bullet.draw() #desenho da bala
        
        

        nave.draw()

        if teclado.key_pressed("ESC"):
            break
        janela.update()
