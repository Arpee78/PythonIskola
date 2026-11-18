minutesAll = int(input("Add meg hány perc alatt végeztél a feladatoddal: "))

hours = minutesAll // 60
minutes = minutesAll % 60

print(f"A tanuló {hours} óra és {minutes} perc alatt teljesítette a feladatot.")