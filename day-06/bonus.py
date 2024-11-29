def trierListe(arrayParam): # fonction job12 & job 15 jour 5

    nombre_coup = 0

    for i in range(len(arrayParam)):
        for x in range(len(arrayParam) - i - 1):
            if arrayParam[x] > arrayParam[x + 1]:
                arrayParam[x], arrayParam[x + 1] = arrayParam[x + 1], arrayParam[x]
                nombre_coup += 1
    return arrayParam, f"COUPS = {nombre_coup}"

ma_liste = [0, 330000, 55, 1, 9, 309, 6]

print(f"Result : {trierListe(ma_liste)}")