import model, pygame
import model_nevazhno

display = pygame.display.set_mode([1500, 1000])

spacex = pygame.image.load("spacex.jpg")

spacex_transform = pygame.transform.scale(spacex, [1500, 1000])


def risovanie_nachalo():
    display.fill([0, 0, 0])

    #Картинки
    display.blit(spacex_transform,[0,0])

    #Тексты

    #Ректы
    pygame.draw.rect(display, [11, 255, 0], model_nevazhno.rect_start)

    #Картинки
    display.blit(model_nevazhno.start,model_nevazhno.rect_start)
    display.blit(model_nevazhno.save_urovenb,model_nevazhno.rect_urovenb)

    pygame.display.flip()
