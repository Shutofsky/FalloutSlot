import pygame
from pygame.locals import *
pygame.init()
from game import *

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

game(screen)