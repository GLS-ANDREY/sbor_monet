import model, pygame
import model_nevazhno

# spisok = pygame.font.get_fonts()
# spisok.sort()
# print(spisok)
display = pygame.display.set_mode([1500, 1000])

pygame.init()
font = pygame.font.SysFont("Fixedsys", 50, True)
spacex = pygame.image.load("spacex.jpg")

spacex_transform = pygame.transform.scale(spacex, [1500, 1000])

start = font.render("START", True, [255, 255, 255])

def risovanie_nachalo():
    display.fill([0, 0, 0])
    display.blit(spacex_transform,[0,0])
    display.blit(start,model_nevazhno.rect_start)
    pygame.display.flip()
