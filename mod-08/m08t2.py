import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='pinja',
         password='1234',
         autocommit=True
         )
def haku(maakoodi):
    sql = f"SELECT DISTINCT type, COUNT(*) FROM airport WHERE iso_country=%s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    return kursori.fetchall()

tilasto = haku(input("Syötä maakoodi: "))
print("Lentokentän tyyppi ja lukumäärä:")
for rivi in tilasto:
    print(f"{rivi[0]}: {rivi[1]}")