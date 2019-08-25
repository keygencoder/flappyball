import random

import pygame

from flappyball.config import *


class Pipeline(object):
    def __init__(self, screen, x):
        self._screen = screen
        self._x = x
        self._y_up = random.randint(0, window_size_y - pipeline_free_space_length)
        self._y_down = self._y_up + pipeline_free_space_length
        self._jumped = False

    def update(self, frame_time):
        self._x = self._x + pipeline_horizontal_speed * frame_time

    def draw(self):
        pygame.draw.rect(self._screen, pipeline_color, [self._x, 0, pipeline_length, self._y_up], 0)
        pygame.draw.rect(self._screen, pipeline_color, [self._x, self._y_down, pipeline_length, window_size_y - self._y_down], 0)

    def is_over_range(self):
        return True if self._x + pipeline_length <= 0 else False

    def get_child(self):
        new_x = self._x + pipeline_length + pipeline_distance
        if new_x > window_size_x:
            return None
        return Pipeline(self._screen, new_x)

    def first_time_been_jumped(self):
        if self._jumped is True:
            return False
        if self._x + pipeline_length <= ball_x_start:
            self._jumped = True
            return True

    def is_hit_ball(self, ball_x, ball_y):
        if (ball_y < self._y_up + ball_radius) or (ball_y > self._y_down - ball_radius):
            if (ball_x > self._x - ball_radius) and (ball_x < self._x + pipeline_length + ball_radius):
                return True
        if (self._x - ball_x) * (self._x - ball_x) + (self._y_up - ball_y) * (self._y_up - ball_y) < ball_radius * ball_radius:
            return True
        if (self._x - ball_x) * (self._x - ball_x) + (self._y_down - ball_y) * (self._y_down - ball_y) < ball_radius * ball_radius:
            return True
        return False
