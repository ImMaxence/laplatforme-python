a = float(input("\n1️⃣ - Entrez la longueur du côté a => "))
b = float(input("\n2️⃣ - Entrez la longueur du côté b => "))
c = float(input("\n3️⃣ - Entrez la longueur du côté c => "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("\nC'est un triangle équilatéral ✅\n")
    elif a == b or b == c or a == c:
        print("\nC'est un triangle isocèle ✅\n")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("\nC'est un triangle rectangle ✅\n")
    else:
        print("\nC'est un triangle quelconque 😬\n")
else:
    print("\nCes longueurs ne peuvent pas former un triangle ❌\n")