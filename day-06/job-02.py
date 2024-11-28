def draw(size: int):
    for item in range(1, size + 1):
        print((' ' * (size - item)) + '/' + (' ' * (item * 2)) + '\\')
    
    print('-' * ((size * 2) + 2)) # + 2 pour les espaces manquants

draw(50)
