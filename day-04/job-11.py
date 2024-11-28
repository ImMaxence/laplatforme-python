def time_to_text(minute):
    if isinstance(minute, int) and minute >= 0:
        heure = minute // 60 # // pour return un nombre entier
        minu = minute - (heure * 60) # convertir les heures en minute - le nombre de minute rentré
        print(str(heure) + "h" + str(minu))
    else:
        print('Erreur')


time_to_text(130)
time_to_text(45)
time_to_text(0)
time_to_text(-20)