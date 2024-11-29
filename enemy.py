from PPlay.sprite import Sprite
from utils import set_scale
import constants


enemy_image = "./assets/enemy.png"

class Enemy:

    def __init__(self):
        set_scale(enemy_image, constants.ENEMY_WIDTH, constants.ENEMY_HEIGTH)

        # Criando uma matriz 2D de sprites (rows x cols)
        self.enemies = [[None for i in range(constants.ENEMY_ROW_NUMBER)] for j in range(constants.ENEMY_COLUMN_NUMBER)]

        for i in range(constants.ENEMY_ROW_NUMBER):
            for j in range(constants.ENEMY_COLUMN_NUMBER):
                enemy = Sprite(enemy_image)
                enemy.set_position(constants.ENEMY_DISTANCE*i + constants.ENEMY_MARGIN, constants.ENEMY_DISTANCE*j + constants.ENEMY_MARGIN)
                self.enemies[i][j] = enemy

        

    
    def draw_enemies(self):
        
        for i in range(constants.ENEMY_ROW_NUMBER):
            for j in range(constants.ENEMY_COLUMN_NUMBER):
                self.enemies[i][j].draw()
                if((self.enemies[constants.ENEMY_ROW_NUMBER - 1][constants.ENEMY_COLUMN_NUMBER - 1].x > constants.WINDOW_WIDTH - constants.ENEMY_WIDTH and constants.enemy_speed > 0) or (self.enemies[0][0].x < 0 and constants.enemy_speed < 0)):
                    self.enemies[i][j].y += constants.ENEMY_MARGIN_TOP_SPEED         

    def move_enemies(self, janela, nave_y):

        output = 0

        if((self.enemies[constants.ENEMY_ROW_NUMBER - 1][constants.ENEMY_COLUMN_NUMBER - 1].x > constants.WINDOW_WIDTH - constants.ENEMY_WIDTH and constants.enemy_speed > 0) or (self.enemies[0][0].x < 0 and constants.enemy_speed < 0)):
            constants.enemy_speed = - constants.enemy_speed
            
        for i in range(constants.ENEMY_ROW_NUMBER):
            for j in range(constants.ENEMY_COLUMN_NUMBER):
                self.enemies[i][j].move_x(constants.enemy_speed*janela.delta_time())
                if(nave_y < self.enemies[i][j].y + constants.ENEMY_HEIGTH):
                    output =  0
                else:
                    output =  1
        return output


