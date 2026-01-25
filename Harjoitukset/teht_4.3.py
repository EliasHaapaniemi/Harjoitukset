syote = input("Anna ensimmäinen luku: ")
if syote != "":
    luku = float(syote)
    pienin = luku
    suurin = luku
    while syote != "":
        luku = float(syote)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

        syote = input("Anna seuraava luku (tyhjä lopettaa): ")
    print(f"Pienin: {pienin}")
    print(f"Suurin: {suurin}")