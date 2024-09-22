import pygame, model, random
from pygame import *

display = display.set_mode([1500, 1000])

init()
font = pygame.font.SysFont("arial", 27, True)
zona = pygame.image.load("zona.png")
moneta = pygame.image.load("Moneta.png")
ilon_mask = pygame.image.load("this_is_ilon_mask.jpg")

moneta_transform = pygame.transform.scale(moneta, [50, 50])
zona_transform = pygame.transform.scale(zona, [400, 1000])
ilon_mask_transform = pygame.transform.scale(ilon_mask, [450, 300])


def risovanie():
    number_tochek = 0
    display.fill([0, 0, 0])

    # Картинки
    display.blit(zona_transform, [1100, 0])
    display.blit(ilon_mask_transform, [500+model.speed_y, 500+model.speed_y])
    model.speed_ilon_mask()
    # Ректы
    # draw.rect(display,[255,255,255],model.rect_monetki,4)
    # Тексты
    monet_sobrano = font.render("Всего собрано " + str(model.bank) + " монет", True, [255, 255, 255])
    vsego_bilo_monet = font.render("Всего появилось " + str(model.mirovoy_bank) + " монет", True, [255, 255, 255])

    while True:
        x_start_pos = 1500 / (model.kol_tochki - 1) * number_tochek
        x_end_pos = 1500 / (model.kol_tochki - 1) * (number_tochek + 1)

        if number_tochek < model.kol_tochki - 1:
            draw.line(display, [34, 175, 41], [x_start_pos, model.randomniy_y_spisok[number_tochek]],
                      # тут берется n элемент
                      [x_end_pos, model.randomniy_y_spisok[number_tochek + 1]], 4)
        number_tochek += 1

        if number_tochek == model.kol_tochki:
            break

    display.blit(vsego_bilo_monet, [0, 30])
    display.blit(monet_sobrano, [0, 0])
    display.blit(moneta_transform, model.rect_monetki)
    pygame.display.flip()
