from classes.auto import Auto

auto1 = Auto("ABC-123", 142)
print("Auton ominaisuudet:")
print("Rekisteritunnus:", auto1.rekisteritunnus)
print("Huippunopeus:", auto1.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto1.nopeus, "km/h")
print("Kuljettu matka:", auto1.matka, "km")