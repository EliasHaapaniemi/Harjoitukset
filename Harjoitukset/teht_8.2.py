import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="salasana",
    autocommit=True
)

cursor = yhteys.cursor()

maakoodi = input("Anna maakoodi (esim. FI): ")

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
"""

cursor.execute(sql, (maakoodi,))
tulokset = cursor.fetchall()

for rivi in tulokset:
    print(f"{rivi[0]}: {rivi[1]} kpl")

cursor.close()
yhteys.close()