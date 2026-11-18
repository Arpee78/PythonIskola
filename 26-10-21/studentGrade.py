points = int(input("Add meg hány pontot érte el a tanuló: "))

if points <= 19:
    print("Elégtelen")
elif 20 <= points  < 27:
    print("Elégséges")
elif 28 <= points < 34:
    print("Közepes")
elif 35 <= points  < 42:
    print("Jó")
else:
    print("Kiváló")