from random import randint

def heitto(b):
    return randint(1,b)

tahkot = int(input("Anna nopan tahkojen yhteismäärä: "))
while True:
    silmaluku = heitto(tahkot)
    print(silmaluku)
    if silmaluku == tahkot:
        break