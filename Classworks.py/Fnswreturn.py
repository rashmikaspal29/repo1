def reverseOrder(name):
    nameList = name.split()
    firstName = nameList[0]
    lastName = nameList[-1]
    return (f"{lastName}, {firstName}")

def main():
    numName = int(input("How many names? "))
    print()

    for i in range(numName):
        fullName = input("Enter full name beginning with first name: ")
        print(f"Reverse it is {reverseOrder(fullName)}")
        print()
main()

    