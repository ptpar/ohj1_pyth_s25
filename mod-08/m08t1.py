import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

def haku(icao_ident: str):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_ident,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return f"{tulos[0][0]}, {tulos[0][1]}"
    return None

#esimkoodit: ESSA, EFHK, 00AA
icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
hakutulos = haku(icao_koodi)
if hakutulos:
    print("Lentokentän nimi ja sijaintikunta:", hakutulos)
else:
    print("ICAO-koodia vastaavaa lentokenttää ei löydy.")

yhteys.close()