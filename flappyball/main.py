import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pygame
from flappyball.config import *
from flappyball.scene.title import Title

pygame.init()
pygame.display.set_caption('flappyball by keygencoder')
screen = pygame.display.set_mode((window_size_x, window_size_y))
Title(screen).run()
