import random
def heita_noppa(tahkot):
    return random.randint(1, tahkot)
tahkojen_maara = int(input("Kuinka monta tahkoa nopassa on? "))
maksimi = tahkojen_maara
tulos = 0
while tulos != maksimi:
    tulos = heita_noppa(tahkojen_maara)
    print(f"Heitit: {tulos}")