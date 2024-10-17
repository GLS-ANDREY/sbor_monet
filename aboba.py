# coding=utf-8
import model, pygame, view_game
import model_nevazhno
pygame.init()
font2 = pygame.font.SysFont("comicsansms", 27, True)
display = pygame.display.set_mode([1500, 1000])

spacex = pygame.image.load("spacex.jpg")

spacex_transform = pygame.transform.scale(spacex, [1500, 1000])


def risovanie_stat_start():
    display.fill([0, 0, 0])
    # Картинки
    display.blit(spacex_transform, [0, 0])
    # Текст
    view_game.risovanie_nadpisi("Текущий уровень:" + str(model_nevazhno.ris_lvl), 0)
    view_game.risovanie_nadpisi("Всего выпало монет:" + str(model.mirovoy_bank), 30)
    view_game.risovanie_nadpisi("Всего собрано монет:" + str(model.bank), 60)
    view_game.risovanie_nadpisi("Всего кликов мышью за игру:" + str(model_nevazhno.clicks), 90)
    view_game.risovanie_nadpisi("Всего Илон Маск пролетел пикселей:" + str(model.pixel), 120)
    pygame.display.flip()
