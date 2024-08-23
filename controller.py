import pygame,model,random
from pygame import *
pygame.key.set_repeat(50)
timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 100)


def allsobitiya():
    global random_append
    s = pygame.event.get()
    for a in s:
        # Закрытие программы на крестик
        if a.type == pygame.QUIT:
            exit()
        if a.type == timer_grafika:
            del model.randomniy_y_spisok[0]
            model.randomniy_y_spisok.append(random_append)
            b = random_append - 50
            c = random_append + 50
            random_append = random.randint(b, c)
