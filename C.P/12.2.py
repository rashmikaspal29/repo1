def mirrorList(myList):
    for index in range(len(myList))-1, -1, -1):
        myList.append(myList[index])