def calcule(num1:int, operator:str, num2:int):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return print("Erreur : division par zéro")
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return print("Erreur : division par zéro")
        return num1 % num2
    else:
        return print("Erreur : opérateur non valide")

toDisplay = calcule(2, "+", 2)
print(toDisplay)
toDisplay = calcule(2, "-", 2)
print(toDisplay)
toDisplay = calcule(2, "*", 2)
print(toDisplay)
toDisplay = calcule(2, "/", 2)
print(toDisplay)
toDisplay = calcule(2, "%", 2)
print(toDisplay)
toDisplay = calcule(-2, "+", -2)
print(toDisplay)
toDisplay = calcule(2, "/", 0)
print(toDisplay)
