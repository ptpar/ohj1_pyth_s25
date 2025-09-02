from random import randint
lkm = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(lkm):
    summa += randint(1,6)

print(summa)