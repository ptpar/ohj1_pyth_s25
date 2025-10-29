import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user',
         password='password',
         autocommit=True
         )
def haku(maakoodi):
    sql = f"SELECT DISTINCT type, COUNT(*) FROM airport WHERE iso_country=%s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print("Lentokentän tyyppi ja lukumäärä:")
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]}")
    else:
        print("Syötetty maakoodi on väärin.")

haku(input("Syötä maakoodi: "))
