szamla = [-1782, -3827, 100000, 4000, -2387, "Béla"]

for elem in szamla:
    if type(elem) == int:
        print(elem, " Szám")
    elif type(elem) == str:
        print(elem, "Szöveg")