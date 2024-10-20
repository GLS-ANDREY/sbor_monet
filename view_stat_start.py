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
    view_game.risovanie_nadpisi("Текущий уровень:" + str(model_nevazhno.stats_read2[4]), 0)
    view_game.risovanie_nadpisi("Всего выпало монет:" + str(model_nevazhno.stats_read2[3]), 30)
    view_game.risovanie_nadpisi("Всего собрано монет:" + str(model_nevazhno.stats_read2[2]), 60)
    view_game.risovanie_nadpisi("Всего кликов мышью за игру:" + str(model_nevazhno.stats_read2[1]), 90)
    view_game.risovanie_nadpisi("Всего Илон Маск пролетел пикселей:" + str(model_nevazhno.stats_read2[0]), 120)
    #Ректы
    pygame.draw.rect(display, [0, 255, 0], model_nevazhno.rect_back)
    #Картинки
    display.blit(model_nevazhno.back,model_nevazhno.rect_back)
    pygame.display.flip()
