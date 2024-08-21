import pygame, model, random
from pygame import *

display = display.set_mode([1000, 1000])

init()
font = pygame.font.SysFont("arial", 27, True)


randomniy_y = random.randint(10, 990)




def risovanie():
    number_tochek = 0
    display.fill([0, 0, 0])

    while True:
        xsp = 1000 / (model.kol_tochki - 1) * number_tochek
        xep = 1000 / (model.kol_tochki - 1) * (number_tochek + 1)
        if number_tochek < model.kol_tochki - 1:
            draw.line(display, [34, 175, 41], [xsp, model.randomniy_y_spisok[number_tochek]],  # тут берется n элемент
                      [xep, model.randomniy_y_spisok[number_tochek + 1]], 5)
        number_tochek += 1

        if number_tochek == model.kol_tochki:
            break
    pygame.display.flip()
