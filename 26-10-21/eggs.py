eggsAll = int(input("Add meg hány tojást tojtak a tyúkok a mai nap: "))

trays = eggsAll // 18
remains = eggsAll % 18

print(f"A szükséges 18db-os tálcák száma {trays} és {remains} tojás maradt.")