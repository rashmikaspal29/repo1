def doubleList(listt):
    numList = []

    for num in listt:
        numList.append(num)
        numList.append(num)
    return numList
def main():
    aList = [3, 2, 5]
    print(doubleList(aList))
    print(aList)
main()


