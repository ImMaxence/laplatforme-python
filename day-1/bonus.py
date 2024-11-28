def searchLetter(paramString):

    array = list(paramString)
    number = array.count("e")

    if number >= 1:
        print("Yes, my string contain the letter : e, " + str(number) + " e present in the string")
    else :
        print("No my string dont contain the letter : e")


my_string = "FLkdslicsnfEkdslksdlkceosocjSdleec"
searchLetter(my_string)