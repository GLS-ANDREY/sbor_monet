import random
from pygame import *
randomniy_y_spisok = []
kol_tochki = random.randint(250, 250)
s = range(kol_tochki)
x_monetki = 1200
y_monetki = 750

nachalo_grafika = random.randint(10, 700)
for a in s:
    randomniy_y_spisok.append(nachalo_grafika)

    b = nachalo_grafika-50
    c = nachalo_grafika+50
    nachalo_grafika = random.randint(b, c)

random_append = randomniy_y_spisok[-1]
def timer_spawna_monetki():
    global x_monetki, y_monetki
    x_monetki = random.randint(1100, 1450)
    y_monetki = random.randint(0, 1500)

def model_in_controller():
    global random_append
    del randomniy_y_spisok[0]
    randomniy_y_spisok.append(random_append)
    random_append = randomniy_y_spisok[-1]

    #Верх
    if random_append <= 0:
        random_ogranichenie1 = 0 - 50
        random_ogranichenie2 = 0 + 50
        random_append = random.randint(random_ogranichenie1, random_ogranichenie2)

    #Посередине
    if random_append > 0:
        random_ogranichenie1 = random_append - 50
        random_ogranichenie2 = random_append + 50
        random_append = random.randint(random_ogranichenie1, random_ogranichenie2)

    #Низ
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
            randomniy_y_spisok[i] -= posledniy_el_minus-1000
    print(randomniy_y_spisok[-1],random_append)



