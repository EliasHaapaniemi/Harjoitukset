import random
maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for _ in range(maara):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Silmälukujen summa on {summa}")