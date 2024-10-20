import pygame, model, model_nevazhno

def allsobitiya_stat_start():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.MOUSEBUTTONDOWN and model_nevazhno.rect_back.collidepoint(a.pos[0], a.pos[1]):
            model.ekran = 1
