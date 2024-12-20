from BaseClass import basic_setup
import constants
from PPlay.sprite import Sprite
from BulletClass import bullets_handler, enemy_bullets_handler

from EnemyTest import enemies
import random
from datetime import datetime


class Play():
    def __init__(self, points = 0):
        self.player = Sprite("./assets/nave.png")
        self.player.x = constants.WINDOW_WIDTH / 2 - constants.NAVE_WIDTH / 2
        self.player.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH - 10
        self.last_shot_time = 0
        self.enemy_shot_time = 0
        self.enemy_shot_delay = 1
        # self.blink_time = 0
        # self.is_blinking = False


        self.vidas = 1
        self.points = points
        self.game_over = False
        self.make_fase_harder = False



    def game(self):
        self.last_shot_time += basic_setup.janela.delta_time()
        self.enemy_shot_time += basic_setup.janela.delta_time()

        basic_setup.janela.draw_text("Vidas: " + str(self.vidas), 10, 10, 30, (0, 0, 0))
        basic_setup.janela.draw_text("Pontos: " + str(self.points), 10, 40, 30, (0, 0, 0))


        for bullet in bullets_handler.bullets:

            if bullet.isActive:
                bullet.move_y(-constants.BULLET_SPEED*basic_setup.janela.delta_time())
                bullet.draw()
                bullet.update()
                if bullet.y < -40:
                    bullet.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
                    bullet.isActive = False

            for enemy_row in (enemies.enemies):
                for enemy in (enemy_row):
                        
                        if enemy and enemy.collided(bullet):
                            self.points+=1
                            enemy_row.remove(enemy)
                            if len(enemy_row) == 0:
                                enemies.enemies.remove(enemy_row)
                            bullet.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
                            bullet.isActive = False
                            self.enemy_shot_delay *= 0.9
                            break

        for bullet in (enemy_bullets_handler.bullets):

            if bullet.isActive:
                bullet.move_y(constants.BULLET_SPEED*basic_setup.janela.delta_time())
                bullet.draw()
                bullet.update()
                if bullet.y > constants.WINDOW_HEIGHT:
                    bullet.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
                    bullet.isActive = False

                if self.player.collided(bullet):
                    self.player.x = constants.WINDOW_WIDTH / 2 - constants.NAVE_WIDTH / 2
                    self.vidas -= 1
                    # self.is_blinking = True
                    if self.vidas == 0:
                        self.game_over = True
                        break
                    # game_over = True
                    # break

            # for i, enemy_row in enumerate(enemies.enemies):
            #     for j, enemy in enumerate(enemy_row):
            #         if(i == 0 and j == 0 and self.last_shot_time > constants.shot_delay):
            #             enemy_bullets_handler.fire_enemy_bullet(enemy.x, enemy.y)

            # if self.player.collided(bullet):
            #     # game_over = True
            #     # break
            #     pass
                            
    

        if basic_setup.teclado.key_pressed("SPACE") and self.last_shot_time > constants.shot_delay:
            self.last_shot_time = 0
            bullets_handler.fire_bullet(self.player.x)


        if self.enemy_shot_time > self.enemy_shot_delay:
            self.enemy_shot_time = 0

            rows_range = len(enemies.enemies) - 1

            if rows_range < 0:
                self.make_fase_harder = True
                return
            i = random.randint(0, rows_range)

            columns_range = len(enemies.enemies[i]) - 1

            if columns_range < 0:
                self.make_fase_harder = True
                return

            j = random.randint(0, columns_range)


            enemy_bullets_handler.fire_enemy_bullet(enemies.enemies[i][j].x, enemies.enemies[i][j].y)

         

        
        # if self.is_blinking:
        #     self.blink()
        
        # else:
        self.player.draw()
        enemies.draw_enemies()
        enemies.move_enemies(self.player.y)
        self.move_player()



    def move_player(self):
        if basic_setup.teclado.key_pressed("RIGHT") and self.player.x < constants.WINDOW_WIDTH - constants.NAVE_WIDTH:
            self.player.move_key_x(constants.nave_speed*basic_setup.janela.delta_time())
        if basic_setup.teclado.key_pressed("LEFT") and self.player.x > 0:
            self.player.move_key_x(constants.nave_speed*basic_setup.janela.delta_time())

    def go_to_another_fase(self, enemies_rows, enemies_columns):
        self.__init__(self.points)
        enemies.__init__(enemies_rows, enemies_columns)

    def gravar_pontuacao(self, user_input):
        arquivo = open("pontuacao.txt", "a")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        text = user_input + ': ' + str(self.points) + ' - Data: ' + data_hora + '\n'
        arquivo.write(text)
        

    # def blink(self):
    #     self.blink_time += basic_setup.janela.delta_time()
    #     self.player.hide()
    #     basic_setup.janela.update()
    #     if self.blink_time > 0.5:
    #         self.blink_time = 0
    #         self.player.unhide()
    #         self.is_blinking = False
        
    #     basic_setup.janela.update()


game = Play

