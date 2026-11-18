osztalyzat = [5, 5, 5, 4, 4, 3, 1]

osszeg = 0
for elem in osztalyzat:
    osszeg += elem

atlag = osszeg / len(osztalyzat)

print(f"A jegyek átlaga: {atlag:.2f}")