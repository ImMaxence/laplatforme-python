def draw_rectangle(width:int,height:int):
    print('-' * width)

    for item in range(height):
        print('|' + (' ' * (width - 2)) + '|') # - les 2 lignes avec les |

    print('-' * width)

draw_rectangle(10, 3)