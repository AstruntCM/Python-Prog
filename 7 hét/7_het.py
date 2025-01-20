# Modulok, csomagok importálása

import random

random.randint(1, 100)

# Ha csak egy adott részt szeretnél importálni
from random import randint

randint(10, 20)

# Egy csomagból mindent importálni akarsz
from random import *

import numpy as np


#----------------------------------------------------------------

# Datetime

import datetime

dt = datetime.datetime(2019, 10, 21, 15, 47, 31, 100000)

print(dt)

# Különbség 2 idő között

dt1 = datetime.datetime(2019, 10, 12, 21, 30, 24)
dt2 = datetime.datetime(2020, 1, 5, 10, 0, 0)

diff = dt2 - dt1

print(diff)

# Átalakitás mondjuk sec-re

print(diff.total_seconds())

# Feladat

tok = input("(ÉÉÉÉ-HH-NN)").split('-')
y, m, d = int(tok[0]), int(tok[1]), int(tok[2])

dt1 = datetime.datetime(y, m, d)
dt2 = datetime.datetime(y, 1, 1)

print((dt1 - dt2).days + 1)

#------------------------------------------------------------------------------

# Time

import time

time.time() # aktuális idő (UNIX időbélyeg)

time.sleep(2) # 2 sec várakozás

# Math

import math

#----------------------------------------------------------------------------------

# Random

import random

random.randint(2, 10) # 2 és 10 között egész random szám

random.uniform(2, 10) # 2 és 10 között valós random szám

random.seed(42) # Véletlen szám generátor alapja

random.choice(['alma', 'körte', 'szilva']) # Elem kisorsolása egy listából

random.sample(range(1, 91), 5) # Visszatevés nélküli mintavétel (Nincs ismétlődés)

# Feladat

text = input('Kérek egy szöveget: ')
print(''.join(random.sample(text, len(text))))