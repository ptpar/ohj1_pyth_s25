from random import randint
from tabulate import tabulate
from mod_09.classes.auto import Auto

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot


    def tunti_kuluu(self):
        for a in self.autot:
            a.kiihdyta(randint(-15, 15))
            a.kulje(1)

    def tulosta_tilanne(self):
        autot2 = [[a.rekisteritunnus, a.huippunopeus, a.nopeus, a.matka] for a in self.autot]
        headers = ["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"]
        print("Autojen ominaisuudet:")
        print(tabulate(autot2, headers=headers, tablefmt="grid"))

    def kilpailu_ohi(self):
        for a in self.autot:
            if a.matka >= self.pituus:
                return True
        return False
