# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

arrayInter = []
sommeTotal = 1 # si multiplie par 0 alors somme = 0

for x in L:
    if 25 <= x <= 90:
        arrayInter.append(x)

for i in arrayInter:
    sommeTotal = sommeTotal * i


print("produit des valeurs dans l'intervalle [25, 90] est : " + str(sommeTotal))
