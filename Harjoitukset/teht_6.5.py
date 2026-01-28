import random
def karsi_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset
alkuperainen = []
for i in range(10):
    alkuperainen.append(random.randint(1, 99))
karsittu = karsi_parittomat(alkuperainen)
print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Karsittu lista (vain parilliset): {karsittu}")
