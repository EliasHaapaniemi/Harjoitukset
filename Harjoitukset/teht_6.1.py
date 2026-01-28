import random
def heita_noppa():
    return random.randint(1, 6)
tulos = 0
while tulos != 6:
    tulos = heita_noppa()
    print(f"Heiton tulos: {tulos}")