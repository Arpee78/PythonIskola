import random

veletlen = random.randint(0,1000)
szamlalo = 0
osszeg = 0

while szamlalo < 10:
    osszeg += veletlen
    szamlalo += 1
    veletlen = random.randint(0, 1000)

print(osszeg)