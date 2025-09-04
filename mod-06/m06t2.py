from random import randint

def heitto(b):
    return randint(1,b)

tahkot = int(input("Anna nopan tahkojen yhteismäärä: "))
silmaluku = 0
kierros = 0
while silmaluku != tahkot:
    silmaluku = heitto(tahkot)
    kierros += 1
    print(f"{kierros}. kierros: {silmaluku}")