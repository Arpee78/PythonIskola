# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 2147483647
def prim(number):

    if number == 0 or number == 1:
        return False

    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

in_number = int(input("Mondj egy számot, megmondom prím szám e: "))
print(prim(in_number))