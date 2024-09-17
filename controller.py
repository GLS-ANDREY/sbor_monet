import pygame,model,random
from pygame import *
pygame.key.set_repeat(50)
timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 50)
type_spawn_monetki = event.custom_type()
time.set_timer(type_spawn_monetki, 1000)


def allsobitiya():
    global random_append
    s = pygame.event.get()

    for a in s:
        if a.type == type_spawn_monetki:
            model.timer_spawna_monetki()
        if a.type == pygame.QUIT:
            exit()

        if a.type == timer_grafika:
            model.model_in_controller()
