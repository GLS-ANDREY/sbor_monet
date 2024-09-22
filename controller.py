import pygame, model, random
from pygame import *

pygame.key.set_repeat(50)

timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 50)

type_spawn_monetki = event.custom_type()
time.set_timer(type_spawn_monetki, 1500)


def allsobitiya():
    global random_append
    s = pygame.event.get()

    for a in s:
        if a.type == type_spawn_monetki:
            model.timer_spawna_monetki()
        if a.type == pygame.MOUSEBUTTONDOWN and model.rect_monetki.collidepoint(a.pos[0], a.pos[1]):
            model.bank += 1
            time.set_timer(type_spawn_monetki, 1500)
            model.timer_spawna_monetki()

        if a.type == pygame.QUIT:
            exit()

        if a.type == timer_grafika:
            model.grafik()
