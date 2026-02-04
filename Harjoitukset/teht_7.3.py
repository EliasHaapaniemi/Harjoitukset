lentoasemat = {}

while True:
    valinta = input("\nValitse: 1 (uusi), 2 (haku), 0 (lopeta): ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Koodia ei löydy.")
    elif valinta == "0":
        print("Heippa!")
        break