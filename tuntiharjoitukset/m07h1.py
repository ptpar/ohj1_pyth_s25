numbers = []
luku = int(input("Syötä luku. Luku 0 keskeyttää ohjelman. "))
while luku != 0:
    numbers.append(luku)
    luku = int(input("Syötä luku. Luku 0 keskeyttää ohjelman. "))
print(list(set(numbers)))