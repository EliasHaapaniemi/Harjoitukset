def laske_summa(luvut):
    yhteensa = 0
    for luku in luvut:
        yhteensa += luku
    return yhteensa
lista = [1, 2, 3, 4, 5]
print(f"Listan summa on: {laske_summa(lista)}")