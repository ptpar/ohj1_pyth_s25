numbers = []
n = input("Anna kokonaisluku. Tyhjä merkkijono keskeyttää ohjelman. ")

while n != "":
    numbers.append(int(n))
    n = input("Anna kokonaisluku. Tyhjä merkkijono keskeyttää ohjelman. ")
if numbers:
    numbers.sort(reverse=True)
    print("Enintään viisi suurinta lukua suuruusjärjestyksessä:")
    print(numbers[:5])