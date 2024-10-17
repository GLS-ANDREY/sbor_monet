import pygame, model, model_nevazhno

def allsobitiya_stat_start():
    s = pygame.event.get()
    for a in s:

        if a.type == pygame.QUIT:
            exit()
