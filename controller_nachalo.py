import pygame, model, model_nevazhno


def allsobitiya_nachalo():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.MOUSEBUTTONDOWN and model_nevazhno.rect_start.collidepoint(a.pos[0], a.pos[1]):
            model.ekran = 0
            model.start_game()
        if a.type == pygame.MOUSEBUTTONDOWN and model_nevazhno.rect_urovenb.collidepoint(a.pos[0], a.pos[1]):
            model_nevazhno.stats_load()
            model.ekran = 3
        if a.type == pygame.QUIT:
            exit()
