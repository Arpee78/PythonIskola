capacity = int(input("Add meg a telefonod tárkapacitását(GB): "))
usedCapacity = float(input("Add meg a jelenleg használt tárterületet a telefonodon(GB): "))

freeCapacity = capacity - usedCapacity

freeCapPercent = freeCapacity / capacity * 100

print(f"A telefonod szabad tárhelye: {freeCapacity} ami {freeCapPercent:.2f}%")