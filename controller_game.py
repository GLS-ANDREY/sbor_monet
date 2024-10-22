import pygame, model, random, time,model_nevazhno

pygame.key.set_repeat(50)

timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 50)

type_ilona_maska = pygame.event.custom_type()
pygame.time.set_timer(type_ilona_maska, 50)

type_speed_ilona_maska = pygame.event.custom_type()
pygame.time.set_timer(type_speed_ilona_maska, 10000)


def allsobitiya():
    global random_append
    s = pygame.event.get()
    for a in s:

        if a.type == pygame.MOUSEBUTTONDOWN:
            model_nevazhno.clicks += 1

        if a.type == model.type_spawn_monetki:
            model.timer_spawna_monetki()

        if a.type == type_speed_ilona_maska:
            model.speed_x += 1
            model.speed_x += 2
            model_nevazhno.ris_lvl += 1

        if a.type == pygame.MOUSEBUTTONDOWN and model.rect_monetki.collidepoint(a.pos[0], a.pos[1]):
            model.bank += 1
            model_nevazhno.bank_stat += 1
            pygame.time.set_timer(model.type_spawn_monetki, 1500)
            model.timer_spawna_monetki()

        if a.type == pygame.QUIT:
            exit()

        if a.type == timer_grafika:
            model.grafik()

        if a.type == type_ilona_maska:
            model.speed_ilon_mask()

        if  a.type == pygame.KEYUP and a.key == pygame.K_ESCAPE:
            model.ekran = 2
