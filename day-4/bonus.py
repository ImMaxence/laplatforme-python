def reverseString(stringParam):
    stringToArray = list(stringParam)
    stringToArray.reverse()
    
    arrayToString = ''.join(stringToArray)
    print(arrayToString)

reverseString('Maxence')