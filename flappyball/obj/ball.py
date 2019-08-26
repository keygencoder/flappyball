import pygame

from flappyball.config import *


class Ball(object):
    def __init__(self, screen):
        self._screen = screen
        self._x = int(window_size_x * 0.2)
        self._y = 0
        self._speed = 0
        self._top = ball_radius
        self._floor = window_size_y - ball_radius
        self.jump = False

    def update(self, frame_time):
        self._y = self._y + self._speed * frame_time + 0.5 * gravity * frame_time * frame_time
        if self.jump:
            self._speed = ball_jump_speed
            self.jump = False
        elif self._y < self._floor:
            self._speed += gravity * frame_time
        elif self._y - self._floor > ball_radius * 0.01:
            self._speed = -self._speed * 0.7
        else:
            self._speed = 0
        if self._y <= self._top:
            self._y = self._top
        elif self._y >= self._floor:
            self._y = self._floor

    def draw(self):
        pygame.draw.circle(self._screen, ball_color, [self._x, int(self._y)], ball_radius, 0)

    def get_position(self):
        return self._x, self._y
