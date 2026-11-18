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

print(f"A legkisebb szám a listában: {legkisebb(szamok)}")
print(f"A legnagyobb szám a listában: {legnagyobb(szamok)}")