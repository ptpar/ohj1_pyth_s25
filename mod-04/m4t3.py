suurin = None
pienin = None
while True:
    luku = input("Anna luku. Tyhjä merkkijono keskeyttää ohjelman. ")
    if luku == "":
        break
    luku = float(luku)
    if suurin is None or luku > suurin:
        suurin = luku
    if pienin is None or luku < pienin:
        pienin = luku


if suurin is not None and pienin is not None:
    print(f"Suurin luku on {suurin} ja pienin luku on {pienin}.")
else:
    print("Et syöttänyt lukua.")
