pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus >= 37:
    print("Kuha on sallitun mittainen")
else:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen. Laske se takaisin järveen.")
    print(f"Pituudesta puuttuu {puuttuu}cm.")