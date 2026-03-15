import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="salasana",
    autocommit=True
)

cursor = yhteys.cursor()

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (icao1,))
coord1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
coord2 = cursor.fetchone()

if coord1 and coord2:
    sijainti1 = (coord1[0], coord1[1])
    sijainti2 = (coord2[0], coord2[1])

    etaisyys = geodesic(sijainti1, sijainti2).kilometers
    print(f"Lentokenttien välinen etäisyys: {etaisyys:.2f} km")

else:
    print("Toista lentokenttää ei löytynyt.")

cursor.close()
yhteys.close()