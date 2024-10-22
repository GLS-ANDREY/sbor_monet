import math
import random, time, pygame, model_nevazhno

def fps():
    model_nevazhno.clock.tick()

#TODO:

def start_game():
    global rect_monetki,rect_ilona_maska,ekran,bank,mirovoy_bank,speed_y,speed_x,pixel

    model_nevazhno.bank_stat = 0
    model_nevazhno.clicks = 0
    pixel = 0

    speed_x = 10
    speed_y = 10

    model_nevazhno.ris_lvl = 1
    bank = 0
    mirovoy_bank = 0

    rect_monetki = pygame.Rect(1200, 750, 50, 50)
    rect_ilona_maska = pygame.Rect(0, 0, 450, 300)

def minus_monetka():
    global bank,ekran
    if rect_monetki.colliderect(rect_ilona_maska):
        bank -= 1
        if bank < 0:
            ekran = 1
            return
        pygame.time.set_timer(type_spawn_monetki, 1500)
        timer_spawna_monetki()


def otbivka():
    if rect_ilona_maska.bottom >= 1000:
        otbivka_niz()
    if rect_ilona_maska.top <= 0:
        otbivka_verx()
    if rect_ilona_maska.x >= 1500:
        vozvrat()


def otbivka_niz():
    global speed_y
    speed_y = -10


def otbivka_verx():
    global speed_y
    speed_y = 10


def vozvrat():
    rect_ilona_maska.x = -700
    model_nevazhno.rekord()
    model_nevazhno.stats_dump()
    model_nevazhno.stats_load()


def speed_ilon_mask():
    global speed_x, speed_y, pixel
    pixel_katet = speed_x * speed_x + speed_y * speed_y
    pixel_koren = math.sqrt(pixel_katet)
    pixel += int(pixel_koren)
    rect_ilona_maska.x += speed_x
    rect_ilona_maska.y += speed_y
    otbivka()
    minus_monetka()


def timer_spawna_monetki():
    global mirovoy_bank,bank
    mirovoy_bank += 1
    rect_monetki.x = random.randint(1100, 1450)
    rect_monetki.y = random.randint(0, 950)
    minus_monetka()


def grafik():
    global random_append
    del randomniy_y_spisok[0]
    randomniy_y_spisok.append(random_append)
    random_append = randomniy_y_spisok[-1]

    # Верх
    if random_append <= 0:
        random_ogranichenie1 = 0 - 50
        random_ogranichenie2 = 0 + 50
        random_append = random.randint(random_ogranichenie1, random_ogranichenie2)

    # Посередине
    if random_append > 0:
        random_ogranichenie1 = random_append - 50
        random_ogranichenie2 = random_append + 50
        random_append = random.randint(random_ogranichenie1, random_ogranichenie2)

    # Низ
    if random_append > 1000:
        random_ogranichenie1 = 1000 - 50
        random_ogranichenie2 = 1000 + 50
        random_append = random.randint(random_ogranichenie1, random_ogranichenie2)

    posledniy_el_minus = randomniy_y_spisok[-1]
    if posledniy_el_minus < 0:
        posledniy_el_minus1 = -posledniy_el_minus
        dlina_spiska = len(randomniy_y_spisok)
        for i in range(0, dlina_spiska):
            randomniy_y_spisok[i] += posledniy_el_minus1

    posledniy_el_minus = randomniy_y_spisok[-1]
    if posledniy_el_minus > 1000:
        dlina_spiska = len(randomniy_y_spisok)
        for i in range(0, dlina_spiska):
            randomniy_y_spisok[i] -= posledniy_el_minus - 1000

start_game()
type_spawn_monetki = pygame.event.custom_type()
pygame.time.set_timer(type_spawn_monetki, 1500)

ekran = 1
pixel = 0
mirovoy_bank = 1
bank = 0
randomniy_y_spisok = []
kol_tochki = random.randint(250, 250)
s = range(kol_tochki)

speed_x = 10
speed_y = 10

nachalo_grafika = random.randint(10, 700)
for a in s:
    randomniy_y_spisok.append(nachalo_grafika)

    b = nachalo_grafika - 50
    c = nachalo_grafika + 50
    nachalo_grafika = random.randint(b, c)

random_append = randomniy_y_spisok[-1]
