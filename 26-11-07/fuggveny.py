def paros_e(halmaz):
    for elem in halmaz:
        if elem % 2 == 0:
            return True
    return False


print(paros_e([7, 17, 31, 42, 19, 123]))
