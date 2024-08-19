import pygame, model, random
from pygame import *

display = display.set_mode([1000, 1000])

init()
font = pygame.font.SysFont("arial", 27, True)

randomniy_y_spisok = []
randomniy_y = random.randint(10, 990)
kol_tochki = random.randint(5, 15)
s = range(kol_tochki)

for a in s:
    randomniy_y_spisok.append(random.randint(10, 700))


def risovanie():
    number_tochek = 0
    display.fill([0, 0, 0])

    while True:
        randomniy_x = 1000 / (kol_tochki - 1) * number_tochek
        if number_tochek < kol_tochki-1:
            draw.line(display, [34, 175, 41], [randomniy_x, randomniy_y_spisok[number_tochek]],
                    [randomniy_x, randomniy_y_spisok[number_tochek + 1]],5)
        number_tochek += 1

        if number_tochek == kol_tochki:
            break
    pygame.display.flip()
