def removeNumber(myList, myNum):
    for index in range(len(myList)-1, -1,-1):
        if myList[index] % myNum == 0:
            myList.remove(myList[index])
        
