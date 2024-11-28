def my_long_word(numberParam:int, stringParam:str):
    stringSplit = stringParam.split()
    emptyArray = []
    
    for item in stringSplit:
        if len(item) >= numberParam:
            emptyArray.append(item)
    
    stringToDisplay = " ".join(emptyArray)
    return stringToDisplay

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))