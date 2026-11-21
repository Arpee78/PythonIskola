lista = []

with open ("utvonalnyilvantartás.txt", "r", encoding="utf-8") as fileBe:
    next(fileBe)
    sor = fileBe.readline()
    while sor:
        lista.append(sor)
        sor = fileBe.readline()



napok = 1
while napok < 32:
    rendszam_halmaz = set()
    for sor in lista:
        darabok = sor.split(";")
        rendszam = darabok[0]
        honap_napja = int(darabok[1])
        km = int(darabok[2])
        if napok == honap_napja:
            rendszam_halmaz.add(rendszam)
    if len(rendszam_halmaz) != 5:
        print(f"A {napok}. napon nem ment mind az összes öt autó.")
    napok += 1



