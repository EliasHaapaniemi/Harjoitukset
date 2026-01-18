luokka = input("Anna hyttiluokka (LUX, A, B tai C): ")

if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen yläpuolella.")
else:
    print("Virheellinen hyttiluokka.")
