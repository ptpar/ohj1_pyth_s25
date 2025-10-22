from random import randint
from mod_09.classes.auto import Auto
from classes.kilpailu import Kilpailu

autot = []
for i in range(1,11):
    autot.append(Auto(f"ABC-{i}", randint(100,200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti_laskin = 0
while not kilpailu.kilpailu_ohi():
    tunti_laskin += 1
    kilpailu.tunti_kuluu()
    if tunti_laskin % 10 == 0:
        print("Kulunut", tunti_laskin, "tuntia.")
        kilpailu.tulosta_tilanne()
print("Kilpailu on päättynyt.", "Kulunut", tunti_laskin, "tuntia.")
kilpailu.tulosta_tilanne()
