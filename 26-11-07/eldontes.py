halmaz = [7,17,31,42,19,123]

eredmeny = False

for elem in halmaz:
    if elem % 2 == 0:
        eredmeny = True

if eredmeny:
    print("Van benn páros szám")
else:
    print("Nincs benn páros szám")
