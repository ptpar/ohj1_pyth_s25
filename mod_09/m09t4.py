from random import randint
from classes.auto import Auto
from tabulate import tabulate

autot = []
for i in range(1,11):
    autot.append(Auto(f"ABC-{i}", randint(100,200)))

kilpailu = True
voittajat = []
while kilpailu:
    for a in autot:
        a.kiihdyta(randint(-15,15))
        a.kulje(1)
        if a.matka >= 10000:
            voittajat.append(a)
            kilpailu = False

print("Voittajat:")
for a in voittajat:
    print(a.rekisteritunnus)
print()

autot2 = [[a.rekisteritunnus, a.huippunopeus, a.nopeus, a.matka] for a in autot]
headers = ["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"]
print("Autojen ominaisuudet:")
print(tabulate(autot2,headers=headers, tablefmt="grid"))
