ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
nombre_arrondi = []

for item in ma_liste:
    int_part = int(item)
    dec_part = item - int_part

    if dec_part >= 0.5:
        nombre_arrondi.append(int_part + 1)
    else:
        nombre_arrondi.append(int_part)

def trierListe(arrayParam): # fonction job12

    for i in range(len(arrayParam)):
        for x in range(len(arrayParam) - i - 1):
            if arrayParam[x] > arrayParam[x + 1]:
                arrayParam[x], arrayParam[x + 1] = arrayParam[x + 1], arrayParam[x]
    return arrayParam

print(trierListe(nombre_arrondi))