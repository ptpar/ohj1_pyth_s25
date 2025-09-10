nimet = set()
nimi = input("Syötä nimi. Tyhjä merkkijono lopettaa ohjelman. ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
    nimi = input("Syötä nimi. Tyhjä merkkijono lopettaa ohjelman. ")
print(nimet)