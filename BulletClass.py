# bullet.py
from PPlay.sprite import Sprite
import constants
from BaseClass import basic_setup


class OneBullet(Sprite):

    def __init__(self, imagem):
        super().__init__(imagem)
        self.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
        self.isActive = False
        self.set_total_duration(1000)

class Bullets():
    def __init__(self, imagem):
        self.bullets = [OneBullet(imagem) for i in range(10)]


        self.bullet_used = 0

    def fire_bullet(self, x):
        self.bullets[self.bullet_used].isActive = True

        self.bullets[self.bullet_used].x = x + constants.NAVE_WIDTH / 2 - 5
        self.bullets[self.bullet_used].draw()
       
        self.bullet_used = (self.bullet_used +1)%10

    def fire_enemy_bullet(self, x, y):
        self.bullets[self.bullet_used].isActive = True

        self.bullets[self.bullet_used].x = x + constants.ENEMY_WIDTH / 2 - 5
        self.bullets[self.bullet_used].y = y + constants.ENEMY_HEIGTH
        self.bullets[self.bullet_used].draw()
       
        self.bullet_used = (self.bullet_used +1)%10

bullets_handler = Bullets("./assets/bullet.png")

enemy_bullets_handler = Bullets("./assets/enemy_bullet.png")

