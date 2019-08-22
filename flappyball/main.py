import sys
import time

import pygame

from flappyball.config import window_size, game_background_color

pygame.init()
pygame.display.set_caption('flappyball')
screen = pygame.display.set_mode(window_size)
screen.fill(game_background_color)

pygame.draw.circle(screen,[255,0,0],[100,100],30,0)
pygame.display.flip()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
