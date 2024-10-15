import model, pygame, model_nevazhno, view_nachalo
import view_game

spacex = pygame.image.load("spacex.jpg")
spacex_transform = pygame.transform.scale(spacex, [1500, 1000])


def risovanie_pauza():
    view_nachalo.display.fill([0, 0, 0])

    # Картинки
    view_nachalo.display.blit(spacex_transform, [0, 0])

    #Ректы
    pygame.draw.rect(view_nachalo.display, [11, 255, 0], model_nevazhno.rect_continue)

    #Тексты

    view_game.risovanie_nadpisi("Текущий уровень:" + str(model_nevazhno.ris_lvl),0)
    view_game.risovanie_nadpisi("Всего выпало монет:" + str(model.mirovoy_bank),30)
    view_game.risovanie_nadpisi("Всего собрано монет:" + str(model.bank),60)
    view_game.risovanie_nadpisi("Всего кликов мышью за игру:" + str(model_nevazhno.clicks),90)
    view_game.risovanie_nadpisi("Всего Илон Маск пролетел пикселей:" + str(model.pixel),120)

    #Картинки
    view_nachalo.display.blit(model_nevazhno.continue_img,model_nevazhno.rect_continue)

    # view_nachalo.display.blit(tekushi_urovenb,[0,0])
    pygame.display.flip()
