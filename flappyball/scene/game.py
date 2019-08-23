import sys

import pygame

from flappyball.config import *
from flappyball.obj.ball import Ball


class Game(object):
    def __init__(self, screen):
        self._screen = screen

    def run(self):
        clock = pygame.time.Clock()
        ball = Ball(self._screen)
        while True:
            frame_time = clock.tick(game_frame) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not ball.dead:
                    ball.jump = True
            self._screen.fill(game_background_color)
            ball.update(frame_time)
            pygame.display.update()
