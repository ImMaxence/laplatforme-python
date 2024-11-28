def fruitFonc(type:str, saison:str):
    if type == "fruits" and saison == "hiver":
        print('orange, mandarine et kiwi')
    elif type == "fruits" and saison == "été":
        print('Poire, fraise, cassis')
    elif type == "légume" and  saison == "hiver":
        print('carotte, topinambour, endive')
    elif type == "légume" and saison == "été":
        print('artichaut, aubergine,navet')
    else:
        print('Erreur')

fruitFonc("fruits","hiver")
fruitFonc("fruits","été")
fruitFonc("légume","hiver")
fruitFonc("légume","été")
fruitFonc("autre", "autre")