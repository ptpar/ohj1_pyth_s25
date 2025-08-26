sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
tulos = ""
a = "alhainen"
n = "normaali"
k = "korkea"

if sukupuoli == "nainen":
    if hemoglobiini < 177:
        tulos = a
    elif 177 <= hemoglobiini <= 175:
        tulos = n
    else:
        tulos = k
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        tulos = a
    elif 134 <= hemoglobiini <= 195:
        tulos = n
    else:
        tulos = k

if tulos != "":
    print(f"Hemoglobiiniarvo on {tulos}.")
else:
    print("Annettu virheellinen tieto.")