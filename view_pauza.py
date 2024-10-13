import model, pygame, model_nevazhno, view_nachalo
import view_game

spacex = pygame.image.load("spacex.jpg")
spacex_transform = pygame.transform.scale(spacex, [1500, 1000])
font = pygame.font.SysFont("comicsansms", 27, True)


def risovanie_pauza():
    view_nachalo.display.fill([0, 0, 0])

    # Картинки
    view_nachalo.display.blit(spacex_transform, [0, 0])

    #Ректы
    pygame.draw.rect(view_nachalo.display, [11, 255, 0], model_nevazhno.rect_continue)

    #Тексты
    #TODO:Сделать что бы все надписи рисовались дефом помощником

    # tekushi_urovenb = font.render("Текущий уровень:" + str(model_nevazhno.ris_lvl), True, [255, 255, 255])
    # vsego_monet = font.render("Всего выпало монет:" + str(model.mirovoy_bank),True,[255,255,255])
    view_game.risovanie_nadpisi("Всего собрано монет:" + str(model.bank),60)

    #Картинки
    view_nachalo.display.blit(model_nevazhno.continue_img,model_nevazhno.rect_continue)
    # view_nachalo.display.blit(tekushi_urovenb,[0,0])
    # view_nachalo.display.blit(vsego_monet,[0,30])

    pygame.display.flip()
