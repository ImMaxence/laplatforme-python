def drawn(numberParam:int):
    tapis = "#" * (numberParam + 1)
    for item in range(0, (numberParam + 1)):
        splitTapis = list(tapis)
        splitTapis[(-1) - (item - 10)] = " "
        niceString = "".join(splitTapis)
        print(niceString)

drawn(10)