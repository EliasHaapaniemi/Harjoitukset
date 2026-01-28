import math
def laske_yksikkohinta(halkaisija_cm, hinta_e):
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala = math.pi * (sade_m ** 2)
    return hinta_e / pinta_ala
d1 = float(input("Pizzan 1 halkaisija (cm): "))
p1 = float(input("Pizzan 1 hinta (€): "))
d2 = float(input("Pizzan 2 halkaisija (cm): "))
p2 = float(input("Pizzan 2 hinta (€): "))
hinta1 = laske_yksikkohinta(d1, p1)
hinta2 = laske_yksikkohinta(d2, p2)
if hinta1 < hinta2:
    print("Ensimmäinen pizza on halvempi neliöhinnaltaan.")
else:
    print("Toinen pizza on halvempi neliöhinnaltaan.")