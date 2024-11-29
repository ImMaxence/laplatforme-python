def calcul(marche, hauteurCm):
    nombreTotalToiletSemaine = 5 * 7 # 5 fois par jour pour 1 semaine
    totalDistanceSemaineCm = (marche * hauteurCm * nombreTotalToiletSemaine) * 2 # * 2 car allez retour
    totalDistanceSemaineM = totalDistanceSemaineCm / 100
    return f"Pour {marche} marches de {hauteurCm} cm, le gardien parcourt {totalDistanceSemaineM} m par semaine"

print(calcul(20, 6))