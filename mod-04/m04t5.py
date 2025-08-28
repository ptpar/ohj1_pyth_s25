kokeilut = 0
paasy = False
while kokeilut < 5:
    tunnus = input("Anna käyttäjätunnus. ")
    salasana = input("Anna salasana. ")
    if tunnus == "python" and salasana == "rules":
        paasy = True
        break
    print("Väärä käyttäjätunnus tai salasana.")
    kokeilut += 1
    
if paasy:
    print("Tervetuloa")
else:
    print("Pääsy evätty")