# bullet.py
import pygame
from PPlay.sprite import Sprite

def create_bullet(x, y):
    bullet = Sprite("./assets/bullet.png")
    bullet.x = x
    bullet.y = y
    return bullet