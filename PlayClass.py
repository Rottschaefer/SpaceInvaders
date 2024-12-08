from BaseClass import basic_setup
import constants
from PPlay.sprite import Sprite
from BulletClass import bullets_handler

from EnemyTest import enemies

class Play():
    def __init__(self):
        self.player = Sprite("./assets/nave.png")
        self.player.x = constants.WINDOW_WIDTH / 2 - constants.NAVE_WIDTH / 2
        self.player.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH - 10
        self.last_shot_time = 0



    def game(self):
        self.last_shot_time += basic_setup.janela.delta_time()


        for bullet in bullets_handler.bullets:

            if bullet.isActive:
                bullet.move_y(-constants.BULLET_SPEED*basic_setup.janela.delta_time())
                bullet.draw()
                bullet.update()
                if bullet.y < -40:
                    bullet.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
                    bullet.isActive = False

            for enemy_row in enemies.enemies:
                for enemy in enemy_row:
                        if enemy and enemy.collided(bullet):
                            # points+=1
                            enemy_row.remove(enemy)
                            bullet.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
                            bullet.isActive = False
                            break
                            
    

        if basic_setup.teclado.key_pressed("SPACE") and self.last_shot_time > constants.shot_delay:
            self.last_shot_time = 0
            bullets_handler.fire_bullet(self.player.x)

        

        self.player.draw()
        enemies.draw_enemies()
        enemies.move_enemies(self.player.y)
        self.move_player()



    def move_player(self):
        if basic_setup.teclado.key_pressed("RIGHT") and self.player.x < constants.WINDOW_WIDTH - constants.NAVE_WIDTH:
            self.player.move_key_x(constants.nave_speed*basic_setup.janela.delta_time())
        if basic_setup.teclado.key_pressed("LEFT") and self.player.x > 0:
            self.player.move_key_x(constants.nave_speed*basic_setup.janela.delta_time())


game = Play

