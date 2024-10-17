import pygame, model, random, model_nevazhno, settings

display = pygame.display.set_mode([settings.width_display, settings.height_display])

rect = model.rect_ilona_maska

pygame.init()
font = pygame.font.SysFont("arial", 27, True)
font2 = pygame.font.SysFont("comicsansms", 27, True)
zona = pygame.image.load("zona.png")
moneta = pygame.image.load("Moneta.png")
ilon_mask = pygame.image.load("this_is_ilon_mask.jpg")

moneta_transform = pygame.transform.scale(moneta, [50, 50])
zona_transform = pygame.transform.scale(zona, [400, 1000])
ilon_mask_transform = pygame.transform.scale(ilon_mask, [450, 300])

def risovanie_nadpisi(nadpis,y,color=[255,255,255]):
    print(nadpis)
    stat_pauza = font2.render(nadpis,True,color)
    display.blit(stat_pauza,[0,y])


def risovanie_game():
    ris_fps = model_nevazhno.clock.get_fps()
    number_tochek = 0
    display.fill([0, 0, 0])

    # Картинки
    display.blit(zona_transform, [1100, 0])
    display.blit(ilon_mask_transform, rect)

    # Ректы
    # pygame.draw.rect(display,[255,255,255],model.rect_monetki,4)
    # pygame.draw.rect(display,[255,255,255],model.rect_ilona_maska,4)

    # Тексты
    risovanie_nadpisi("Всего собрано " + str(model.bank) + " монет",0)
    risovanie_nadpisi("Всего появилось " + str(model.mirovoy_bank) + " монет", 30)
    risovanie_nadpisi("Уровень: " + str(model_nevazhno.ris_lvl),60)
    risovanie_nadpisi("FPS:" + str(int(ris_fps)), 90,[0,255,0])

    while True:
        x_start_pos = 1500 / (model.kol_tochki - 1) * number_tochek
        x_end_pos = 1500 / (model.kol_tochki - 1) * (number_tochek + 1)

        if number_tochek < model.kol_tochki - 1:
            pygame.draw.line(display, [34, 175, 41], [x_start_pos, model.randomniy_y_spisok[number_tochek]],
                             # тут берется n элемент
                             [x_end_pos, model.randomniy_y_spisok[number_tochek + 1]], 4)
        number_tochek += 1

        if number_tochek == model.kol_tochki:
            break

    display.blit(moneta_transform, model.rect_monetki)
    pygame.display.flip()
