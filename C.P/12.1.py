def changeOddsToOpposite(myList):
    for index in range(len(myList)):
        if myList[index] % 2 == 1:
            myList[index] = (-1) * (myList[index])
    