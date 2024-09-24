import random
from pygame import *

mirovoy_bank = 1
bank = 0
randomniy_y_spisok = []
kol_tochki = random.randint(250, 250)
s = range(kol_tochki)

dvizhenie_x = 1
dvizhenie_y = 1

rect_monetki = Rect(1200, 750, 50, 50)
rect_ilona_maska = Rect(500, 500, 450, 300)

nachalo_grafika = random.randint(10, 700)
for a in s:
    randomniy_y_spisok.append(nachalo_grafika)

    b = nachalo_grafika - 50
    c = nachalo_grafika + 50
    nachalo_grafika = random.randint(b, c)

random_append = randomniy_y_spisok[-1]


def otskok_ilona_maska():
    global dvizhenie_y
    dvizhenie_y = -dvizhenie_y

def speed_ilon_mask():
    global dvizhenie_x, dvizhenie_y
    rect_ilona_maska.x = 500
    rect_ilona_maska.y = 500
    rect_ilona_maska.x += dvizhenie_x
    rect_ilona_maska.y += dvizhenie_y
    dvizhenie_x += 3
    dvizhenie_y += 3


def timer_spawna_monetki():
    global mirovoy_bank
    mirovoy_bank += 1
    rect_monetki.x = random.randint(1100, 1450)
    rect_monetki.y = random.randint(0, 950)



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
