def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            prochain_multiple_5 = (note // 5 + 1) * 5
            if prochain_multiple_5 - note < 3: # si la difference est de -3 on arrondit
                arrondies.append(prochain_multiple_5)
            else:
                arrondies.append(note)
    return arrondies

notes = [83, 82, 67, 34, 88, 92, 56]
print(arrondir_notes(notes))
