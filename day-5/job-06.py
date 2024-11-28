ma_liste = [1, 2, 3, 4, 5]

def swapData(arrayPram):
    if len(arrayPram) > 1:
        arrayPram[0], arrayPram[-1] =  arrayPram[-1], arrayPram[0]
        return arrayPram
    else:
        return 'Rentrer une liste'

print(ma_liste)
print(swapData(ma_liste))