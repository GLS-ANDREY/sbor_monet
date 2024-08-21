import pygame,model,random
from pygame import *
pygame.key.set_repeat(50)

def allsobitiya():
    s = pygame.event.get()
    for a in s:
        # Закрытие программы на крестик
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            del model.randomniy_y_spisok[0]
            model.randomniy_y_spisok.append(random.randint(10, 700))