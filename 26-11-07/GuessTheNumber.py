import random

lower_limit = 1
upper_limit = 100

number = random.randint(lower_limit, upper_limit)

print(f"Gondoltam egy számra {lower_limit} és {upper_limit} között, találd ki!")

yourNumber = int(input("Írj be egy számot: "))

count = 1

while yourNumber != number:
    if number < yourNumber:
        print("Nem talált! A szám kisebb!")
    else:
        print("Nem talált! A szám nagyobb!")
    print("")
    yourNumber = int(input("Írj be egy számot: "))
    count += 1
    print(f"Eddig {count} próbálkozásod volt")

print(f"Talált! A szám {number}")
