from PPlay.sprite import Sprite
from BaseClass import basic_setup
from utils import set_scale
import constants


enemy_image = "./assets/enemy.png"

class Enemy:

    def __init__(self, enemy_rows = constants.ENEMY_ROW_NUMBER, enemy_columns = constants.ENEMY_COLUMN_NUMBER):
        set_scale(enemy_image, constants.ENEMY_WIDTH, constants.ENEMY_HEIGTH)

        # Criando uma matriz 2D de sprites (rows x cols)
        self.enemies = []
        for i in range(enemy_rows):
            row = []
            for j in range(enemy_columns):
                enemy = Sprite(enemy_image)
                enemy.set_position(j * (constants.ENEMY_MARGIN + constants.ENEMY_DISTANCE), 
                                   i * (constants.ENEMY_MARGIN + constants.ENEMY_DISTANCE))
                row.append(enemy)
            self.enemies.append(row)
        self.enemie_rows = enemy_rows
        self.enemie_columns = enemy_columns

        

    
    def draw_enemies(self):
        
        for i in range(self.enemies.__len__()):
            for j in range(self.enemies[i].__len__()):
                if(self.enemies[i][j]):
                    self.enemies[i][j].draw()
                           

    def move_enemies(self, player_y):

        output = 0

        for i in range(self.enemies.__len__()):
            for j in range(self.enemies[i].__len__()):
                if(self.enemies[i][j]):
                    if((self.enemies[i][j].x > constants.WINDOW_WIDTH - constants.ENEMY_WIDTH and constants.enemy_speed > 0) or (self.enemies[0][0].x < 0 and constants.enemy_speed < 0)):
                            constants.enemy_speed = - constants.enemy_speed
                            self.go_down()


                    self.enemies[i][j].move_x(constants.enemy_speed*basic_setup.janela.delta_time())
                    if(player_y < self.enemies[i][j].y + constants.ENEMY_HEIGTH):
                        output =  0
                    else:
                        output =  1
        return output
    

    def go_down(self):
        for i in range(self.enemies.__len__()):
            for j in range(self.enemies[i].__len__()):
                if(self.enemies[i][j]):
                    self.enemies[i][j].move_y(constants.ENEMY_MARGIN_TOP_SPEED)



enemies = Enemy()
