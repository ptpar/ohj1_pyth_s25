from random import randint

def heitto():
    return randint(1,6)

while True:
    silmaluku = heitto()
    print(silmaluku)
    if silmaluku == 6:
        break
