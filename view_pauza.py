import model, pygame, model_nevazhno, view_nachalo

spacex = pygame.image.load("spacex.jpg")
spacex_transform = pygame.transform.scale(spacex, [1500, 1000])

def risovanie_pauza():
    view_nachalo.display.fill([0, 0, 0])

    # Картинки
    view_nachalo.display.blit(spacex_transform, [0, 0])

    #Ректы
    pygame.draw.rect(view_nachalo.display, [11, 255, 0], model_nevazhno.rect_continue)

    #Картинки
    view_nachalo.display.blit(model_nevazhno.continue_img,model_nevazhno.rect_continue)

    pygame.display.flip()
