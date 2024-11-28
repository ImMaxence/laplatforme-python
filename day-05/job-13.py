ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
uniqueNumberArray = []

for item in ma_liste:
    if item not in uniqueNumberArray:
        uniqueNumberArray.append(item)

print(uniqueNumberArray)
