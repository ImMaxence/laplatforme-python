ma_liste = [0, 330000, 55, 1, 9, 309, 6]

def trierListe(arrayParam):

    for i in range(len(arrayParam)):
        for x in range(len(arrayParam) - i - 1):
            if arrayParam[x] > arrayParam[x + 1]:
                arrayParam[x], arrayParam[x + 1] = arrayParam[x + 1], arrayParam[x]
    return arrayParam

print(trierListe(ma_liste))
