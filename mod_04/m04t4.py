import random
luku = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku 1-10 välillä: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break