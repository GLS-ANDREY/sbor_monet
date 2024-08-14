import pygame, model,random
from pygame import *

display = display.set_mode([1000, 1000])

init()
font = pygame.font.SysFont("arial", 27, True)

randomniy_y_spisok = []
randomniy_y = random.randint(10,990)
kol_tochki = random.randint(5,15)
s = range(kol_tochki)

for kol_tochki in s:
    randomniy_y_spisok.append(random.randint(10, 700))

def risovanie():
    global number_tochek,kol_tochki
    number_tochek = 0
    display.fill([0, 0, 0])

    while True:
        draw.circle(display, [100,100,100], [1000 / (kol_tochki-1) * number_tochek, randomniy_y_spisok[number_tochek]], 5)
        number_tochek += 1
        if number_tochek == kol_tochki:
            break
    print(randomniy_y_spisok)
    pygame.display.flip()
