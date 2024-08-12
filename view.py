import pygame, model,random
from pygame import *

display = display.set_mode([1000, 1000])
init()
font = pygame.font.SysFont("arial", 27, True)
x_grafik = 40
kol_tochki = random.randint(5,15)
randomniy_y = random.randint(10,990)
randomniy_y_spisok = [kol_tochki]

def risovanie():
    randomniy_y_spisok.append(1)
    # print(randomniy_y_spisok)
    number_tochek = 0
    display.fill([0, 0, 0])
    draw.line(display, [25,255,0], [0,800],[x_grafik+320,530],5)
    draw.line(display, [25,255,0], [x_grafik+320,530],[x_grafik+640,900],5)
    draw.line(display, [25,255,0], [x_grafik+640,900],[x_grafik+960,200],5)

    while True:
        draw.circle(display, [100,100,100], [1000 / (kol_tochki-1) * number_tochek, randomniy_y_spisok[random.randint]], 5)
        number_tochek += 1
        if number_tochek == kol_tochki:
            break
    pygame.display.flip()
