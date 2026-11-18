szoveg = input("Írj be egy szöveget: ")

vanE = False
for betu in szoveg.lower():
    if betu == "a":
        vanE = True
        break

if vanE:
    print("Van benn 'a' betű")
else:
    print("Nincs 'a' betű")