import mysql.connector
#host='127.0.0.1'
#host='localhost'
#ssh pinja@127.0.0.1
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='pinja',
         password='1234',
         autocommit=True
         )


kysely1 = "SELECT name FROM airport WHERE iso_country = 'FI' and type ='large_airport'"
print(kysely1)
kursori = yhteys.cursor()
kursori.execute(kysely1)
tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi[0])


"""
myös:
yhteys.cursor(dictionary=True))

"""