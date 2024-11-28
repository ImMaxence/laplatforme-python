def positifOrNegative(nombre:int):
    if nombre >= 0:
        print('Nombre positif')
    elif nombre < 0:
        print('Nombre négatif')
    else:
        print('Erreur')

positifOrNegative(2)
positifOrNegative(0)
positifOrNegative(-10)