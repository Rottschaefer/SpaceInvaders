
import pygame

# Dimensões da janela usando pygame
info = pygame.display.Info()
WINDOW_WIDTH = info.current_w * 0.7
WINDOW_HEIGHT = info.current_h * 0.7


# Dimensões dos botões
BUTTON_WIDTH = 400 #Largura dos botões
BUTTON_HEIGHT = 100 #Altura dos botões
BUTTON_MARGIN_TOP = 125 #Posição vertical  inicial do primeiro botão
BUTTON_MARGIN = 150  #Espaçamento entre os botões

# Cores
TEXT_COLOR = (255, 255, 255)
HOVER_TEXT_COLOR = (255, 0, 0)

#Tamanho da fonte do menu
MENU_FONT_SIZE = 36

#Tamanho da nave
NAVE_WIDTH = 80
NAVE_HEIGTH = 80

BULLET_SPEED = 500

shot_delay = 0.5

nave_speed = 500

desired_fps = 100

#Dados para o inimigo

ENEMY_ROW_NUMBER = 3
ENEMY_COLUMN_NUMBER = 5
ENEMY_WIDTH = 115
ENEMY_HEIGTH = 90
ENEMY_DISTANCE = 100
ENEMY_MARGIN = WINDOW_WIDTH*0.01
ENEMY_MARGIN_TOP_SPEED = 100

enemy_speed = 150