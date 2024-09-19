import pygame,model,random
from pygame import *
pygame.key.set_repeat(50)

timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 50)

type_spawn_monetki = event.custom_type()
time.set_timer(type_spawn_monetki, 2000)



def allsobitiya():
    global random_append
    s = pygame.event.get()

    pos_mouse = pygame.mouse.get_pos()
    tik_po_rect = model.rect_monetki.collidepoint(pos_mouse[0], pos_mouse[1])

    for a in s:
        if a.type == type_spawn_monetki:
            model.timer_spawna_monetki()

        if a.type == pygame.MOUSEBUTTONDOWN and tik_po_rect:
            print(1)

        if a.type == pygame.QUIT:
            exit()

        if a.type == timer_grafika:
            model.grafik()
