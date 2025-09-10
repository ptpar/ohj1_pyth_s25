vuodenajat =  ("kevät", "kesä", "syksy", "talvi")
kk = int(input("Syötä kuukauden numero: "))
if 3 <= kk <= 5:
    i = 0
elif 6 <= kk <= 8:
    i = 1
elif 9 <= kk <= 11:
    i = 2
else:
    i = 3
print(f"{kk}. kuukausi kuuluu vuodenaikaan {vuodenajat[i]}.")