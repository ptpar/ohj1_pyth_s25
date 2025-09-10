import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='pinja',
         password='1234',
         autocommit=True
         )

def haku(icao_ident: str):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_ident,))
    tulos = kursori.fetchall()
    return f"{tulos[0][0]}, {tulos[0][1]}"

icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
print(haku(icao_koodi))