from PPlay.sprite import Sprite

enemy_image = "./assets/enemy_boss.png"


class EnemyBoss(Sprite):
    def __init__(self):
        super().__init__(enemy_image)
        self.vidas = 2

