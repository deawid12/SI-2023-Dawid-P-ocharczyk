import numpy as np
import pandas as pd
import csv
import math

# Zad 3
house = np.loadtxt('house-votes-84.txt', dtype=str)
house_type = np.loadtxt('house-votes-84-type.txt', dtype=str)

# a)
print("3a) Symbole Klas decyzyjnych:")
sym_klas_dec = np.unique(house[:, 16])
print(sym_klas_dec)

# b)
print("\n3b) Wielkość klas decyzyjnych:")
ile=[0]*len(sym_klas_dec)

for i in range(len(sym_klas_dec)):
    for j in house[:, 16]:
        if sym_klas_dec[i] == j:
            ile[i] = ile[i] +1
    print(sym_klas_dec[i], "=", ile[i])

# c)
print("\n3c) brak atrybutów numerycznych")

# d)
print("\n3d) Liczba różnych dostępnych wartości")
for i in range(16):
    print("Atrybut numer",i,"| Liczba atrybutów=",len(np.unique(house[:, i])))

# e)
print("\n3e) Lista wartości")
for i in range(16):
    print("Atrybut numer",i,"| Lista=", np.unique(house[:, i]))

# f)
print("\n3f) brak atrybutów numerycznych")

