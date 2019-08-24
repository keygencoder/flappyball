import pygame

from flappyball.config import *


class Pipeline(object):
    def __init__(self, screen):
        self._screen = screen
        self._x = window_size_x
        self._y = window_size_y

    def update(self, frame_time):
        self.draw()

    def draw(self):
        pygame.draw.rect(self._screen, pipeline_color, [250, 150, 300, 200], 0)
