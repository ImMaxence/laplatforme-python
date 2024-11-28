L = list(range(1,6))

def calculerL3():
    somme = L[2] + L[4]
    L[3] = somme
    return L

print(L)
print(L[1])
print(calculerL3())
print(L[-1])