# nombre premier => seulement divisible par lui meme ou 1

def nbPremier(numberParam):
    for x in range(2, numberParam):
        if numberParam % x == 0:
            return False
    return True

for i in range(2, 1001):
    if nbPremier(i):
        print(i)