import pygame

from flappyball.config import *
from flappyball.scene.game import Game

pygame.init()
pygame.display.set_caption(window_name)
screen = pygame.display.set_mode((window_size_x, window_size_y))
screen.fill(game_background_color)
game = Game(screen)
game.run()
