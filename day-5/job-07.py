L = [8, 24, 48, 2, 16]

nombreMultiple = 0

for x in L:
    print(x)
    if x % 3 == 0:
        nombreMultiple += 1

print("Nombre de multiple de 3 : " + str(nombreMultiple))