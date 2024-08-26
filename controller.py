import pygame,model,random
from pygame import *
pygame.key.set_repeat(50)
timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 100)
random_append = model.randomniy_y_spisok[-1]
posledniy_el = model.randomniy_y_spisok[-1]
d = 50
e = 10
#TODO: График вышел вверх на столько скольки равен последний элемент списка, Схема сдвига графика: все точки сдвинуть на столько на сколько вышел график
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
            b = random_append - d
            c = random_append - e
            random_append = random.randint(b, c)
