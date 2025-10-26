class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi} - {self.kirjoittaja}, {self.sivumaara} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, päätoimittaja {self.paatoimittaja}")

# Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua)
Lehti("Aku Ankka", "Aki Hyyppä").tulosta_tiedot()
Kirja("Rosa Liksom", "Hytti n:o 6", 200).tulosta_tiedot()