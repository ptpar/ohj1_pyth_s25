from random import randint

def heitto():
    return randint(1,6)

silmaluku = 0
while silmaluku != 6:
    silmaluku = heitto()
    print(silmaluku)
