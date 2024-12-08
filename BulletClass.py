# bullet.py
from PPlay.sprite import Sprite
import constants
from BaseClass import basic_setup

def create_bullet(x, y):
    bullet = Sprite("./assets/bullet.png")
    bullet.x = x
    bullet.y = y

    return bullet

class OneBullet(Sprite):

    def __init__(self):
        super().__init__("./assets/bullet.png")
        self.y = constants.WINDOW_HEIGHT - constants.NAVE_HEIGTH + 20
        self.isActive = False
        self.set_total_duration(1000)

class Bullets():
    def __init__(self):
        self.bullets = [OneBullet() for i in range(10)]


        self.bullet_used = 0

    def fire_bullet(self, x):
        self.bullets[self.bullet_used].isActive = True

        self.bullets[self.bullet_used].x = x + constants.NAVE_WIDTH / 2 - 5
        self.bullets[self.bullet_used].draw()
       
        self.bullet_used = (self.bullet_used +1)%10

bullets_handler = Bullets()

