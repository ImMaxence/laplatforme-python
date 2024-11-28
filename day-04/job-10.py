def verif(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        print('Votre nombre est bien un nombre positif')
        if nombre % 2 == 0:
            return str(nombre) + " est pair"
        else:
            return str(nombre) + " est impair"
    else:
        return str(nombre) + " : valeur non valide"

print(verif(2))
print(verif(0))
print(verif(-2))
print(verif("text"))
print(verif(30.5))