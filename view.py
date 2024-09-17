import pygame, model, random
from pygame import *

display = display.set_mode([1500, 1000])

init()
font = pygame.font.SysFont("arial", 27, True)
zona = pygame.image.load("zona.png")
moneta = pygame.image.load("Moneta.png")
moneta_transform = pygame.transform.scale(moneta, [300, 300])
zona_transform = pygame.transform.scale(zona, [400, 1000])


def risovanie():
    number_tochek = 0
    display.fill([0, 0, 0])

    display.blit(zona_transform,[1100,0])
    display.blit(moneta_transform, [model.x_monetki, model.y_monetki])
    while True:
        x_start_pos = 1500 / (model.kol_tochki - 1) * number_tochek
        x_end_pos = 1500 / (model.kol_tochki - 1) * (number_tochek + 1)
        if number_tochek < model.kol_tochki - 1:
            draw.line(display, [34, 175, 41], [x_start_pos, model.randomniy_y_spisok[number_tochek]],  # тут берется n элемент
                      [x_end_pos, model.randomniy_y_spisok[number_tochek + 1]], 4)
        number_tochek += 1

        if number_tochek == model.kol_tochki:
            break
    pygame.display.flip()