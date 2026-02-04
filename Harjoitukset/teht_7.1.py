vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kk = int(input("Anna kuukauden numero: "))
indeksi = (kk % 12) // 3
print(f"{kk}. kuukausi kuuluu vuodenaikaan: {vuodenajat[indeksi]}")