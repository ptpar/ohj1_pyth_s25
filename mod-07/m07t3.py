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
    sql = f"SELECT name FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_ident,))
    tulos = kursori.fetchall()
    return tulos[0][0]

print("Komennot:\n"
    "0: ohjelman lopetus\n"
    "1: syötä uusi lentoasema\n"
    "2: hae lentoaseman tiedot")
k = input("Komento: ")

while k=="1" or k=="2":
    if k == "1":
        icao1 = input("Lentoaseman ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
    else:
        icao2 = input("Lentoaseman ICAO-koodi: ")
        print(haku(icao2))
    k = input("Komento: ")
