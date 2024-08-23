import random
from pygame import *

randomniy_y_spisok = []
kol_tochki = random.randint(75, 250)

s = range(kol_tochki)

random_append = random.randint(10, 700)
for a in s:
    randomniy_y_spisok.append(random_append)
    b = random_append-50
    c = random_append+50
    random_append = random.randint(b, c)
