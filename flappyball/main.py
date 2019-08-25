import os
import sys

from flappyball.scene.title import Title

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pygame
from flappyball.config import *

pygame.init()
pygame.display.set_caption(game_name)
screen = pygame.display.set_mode((window_size_x, window_size_y))
Title(screen).run()
