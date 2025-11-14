def doubleList(myList):
    newList = []

    for item in myList:
        newList.append(item)
        newList.append(item)
    return newList
print(doubleList([2, 3, 4, 5]))