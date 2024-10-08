import pygame, model, model_nevazhno

def allsobitiya_pauza():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.MOUSEBUTTONDOWN and model_nevazhno.rect_continue.collidepoint(a.pos[0], a.pos[1]):
            model.ekran = 0
        if  a.type == pygame.KEYDOWN and a.key == pygame.K_ESCAPE:
            model.ekran = 0
        if a.type == pygame.QUIT:
            exit()