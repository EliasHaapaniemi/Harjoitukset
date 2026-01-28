def gallonat_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    g = float(input("Syötä gallonat (negatiivinen lopettaa): "))
    if g < 0:
        break
    print(f"{g} gallonaa on {gallonat_litroiksi(g):.2f} litraa.")
