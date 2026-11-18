import random

szamok = []

for i in range(1,100):
    szamok.append(random.randint(-100,500))

def legkisebb(veletlenek):
    legkisebb = veletlenek[0]
    for i in veletlenek:
        if i < legkisebb:
            legkisebb = i
    return legkisebb

def legnagyobb(veletlenek):
    legnagyobb = veletlenek[0]
    for i in veletlenek:
        if i > legnagyobb:
            legnagyobb = i
    return legnagyobb

def negativszamok(veletlenek):
    count = 0
    for i in veletlenek:
        if i < 0:
            count += 1
    return count

print(f"A legkisebb szám a listában: {legkisebb(szamok)}")
print(f"A legnagyobb szám a listában: {legnagyobb(szamok)}")
print(f"A negatív számok száma a listában: {negativszamok(szamok)}")