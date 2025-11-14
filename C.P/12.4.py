def allLess(myList, value):
    
    for index in range(len(myList)):
        
        if myList[index] >= value:
            
            return False
    return True