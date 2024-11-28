chaine = list("abcdefghijklmnopqrstuvwxyz") * 3 # à modifier, 10 ca fait beaucoup
longueurArray = len(chaine)
stringToDisplay = []
x = 0

while x < longueurArray:
    stringToDisplay.append(chaine[x])
    toDisplay = "".join(stringToDisplay)
    print(toDisplay)
    x = x + 1