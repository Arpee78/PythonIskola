lista = []

with open ("utvonalnyilvantartás.txt", "r", encoding="utf-8") as fileBe:
    next(fileBe)
    sor = fileBe.readline()
    while sor:
        lista.append(sor)
        sor = fileBe.readline()

    keresett_rendszam = input("Add meg a keresett rendszámot: ")
    megvan = False
    utakszama = 0
    adott_nap = int(input("Add meg a hónap napját: "))
    összkm = 0
    auto_km = 0

for sor in lista:
    darabok = sor.split(";")
    rendszam = darabok[0]
    honap_napja = int(darabok[1])
    km_a_napon = int(darabok[2])
    if keresett_rendszam == rendszam:
        megvan = True
        utakszama += 1
        auto_km += km_a_napon
    if honap_napja == adott_nap:
        összkm += km_a_napon
print(f"Ez az autó {utakszama} alkalommal volt úton és {auto_km} km-t tett meg a hónap során.")
print(f"A hónap {adott_nap}. napján összesen {összkm} km-t tett meg a flotta.")




