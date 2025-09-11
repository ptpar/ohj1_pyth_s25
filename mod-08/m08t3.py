import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

def haku(icao_ident):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql,(icao_ident,))
    tulos = kursori.fetchall()
    return tulos

#esimkoodit: ESSA, EFHK
koord1 = haku(input("Syötä 1. lentokentän ICAO-koodi: "))
koord2 = haku(input("Syötä 2. lentokentän ICAO-koodi: "))

if koord1 and koord2:
    print("Lentokenttien välinen etäisyys:")
    print(f"{distance.distance(koord1, koord2).km:.2f} kilometriä.")
else:
    print("Virheellinen ICAO-koodi/koodit.")