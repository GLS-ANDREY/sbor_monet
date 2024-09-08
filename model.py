import random
from pygame import *
#TODO: Рулить вероятностью, не позволять улетать вниз
randomniy_y_spisok = []
kol_tochki = random.randint(75, 250)
s = range(kol_tochki)


nachalo_grafika = random.randint(10, 700)
for a in s:
    randomniy_y_spisok.append(nachalo_grafika)

    b = nachalo_grafika-50
    c = nachalo_grafika+50
    nachalo_grafika = random.randint(b, c)

random_append = randomniy_y_spisok[-1]
def model_in_controller():
    global random_append
    del randomniy_y_spisok[0]
    randomniy_y_spisok.append(random_append)
    random_ogranichenie1 = random_append - 50
    random_ogranichenie2 = random_append + 50
    random_append_old = random_append
    random_append = random.randint(random_ogranichenie1, random_ogranichenie2)
    print(random_append-random_append_old)

    posledniy_el = randomniy_y_spisok[-1]
    if posledniy_el < 0:
        posledniy_el_plus = -posledniy_el
        dlina_spiska = len(randomniy_y_spisok)
        for i in range(0, dlina_spiska):
            randomniy_y_spisok[i] += posledniy_el_plus