from mod_09.classes.auto import Auto


class Sahkoauto(Auto):
    def __init__(self, akkukapasiteetti, rekisteritunnus, huippunopeus):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, bensatankin_koko, rekisteritunnus, huippunopeus):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)


# (ABC-15, 180 km/h, 52.5 kWh)
sahkoauto1 = Sahkoauto(52.5, "ABC-15", 180)
sahkoauto1.nopeus = 100
print(f"Auton {sahkoauto1.rekisteritunnus} matkamittarilukemat ennen 3 h ajomatkaa ja jälkeen:")
print(sahkoauto1.matka)
sahkoauto1.kulje(3)
print(sahkoauto1.matka)

# (ACD-123, 165 km/h, 32.3 l)
polttomoottoriauto1 = Polttomoottoriauto(32.3, "ACD-123", 165)
polttomoottoriauto1.nopeus = 100
print(f"Auton {polttomoottoriauto1.rekisteritunnus} matkamittarilukemat ennen 3 h ajomatkaa ja jälkeen:")
print(polttomoottoriauto1.matka)
polttomoottoriauto1.kulje(3)
print(polttomoottoriauto1.matka)
