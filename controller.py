import pygame
from pygame import *

def allsobitiya():
    s = pygame.event.get()
    for a in s:
        # Закрытие программы на крестик
        if a.type == pygame.QUIT:
            exit()