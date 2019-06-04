import pygame
from pygame.locals import *
pygame.init()
from game import *

screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)

game(screen)