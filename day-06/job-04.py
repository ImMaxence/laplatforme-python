message = "Ceci est mon message"
decalageValue = 6
alpha1 = list(map(chr, range(97, 123))) # a à z
alpha2 = list(map(chr, range(65, 91))) # A à Z

def decalage(deca:int, message:str):
    result = ""
    for item in message:
        if item in alpha1:
            index = alpha1.index(item)
            result += alpha1[(index + deca) % 26]
        elif item in alpha2:
            index = alpha2.index(item)
            result += alpha2[(index + deca) % 26]
        else:
            result += item # si caractere non alphanumerique alors ne rien faire
    
    return result

message_chiffre = decalage(decalageValue, message)
print(message_chiffre)