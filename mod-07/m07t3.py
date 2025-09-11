asemat = {"ESSA": "Stockholm-Arlanda Airport", "EFHK": "Helsinki Vantaa Airport"}

print("Komennot:\n"
    "0: ohjelman lopetus\n"
    "1: syötä uusi lentoasema\n"
    "2: hae lentoaseman tiedot")
k = input("Komento: ")

while k=="1" or k=="2":
    if k == "1":
        icao = input("Lentoaseman ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        asemat[icao] = nimi
    else:
        icao = input("Lentoaseman ICAO-koodi: ")
        if icao in asemat:
            print(f"Lentokenttä {icao} on {asemat[icao]}.")
        else:
            print(f"Lentokenttää {icao} ei löydy.")
    k = input("Komento: ")