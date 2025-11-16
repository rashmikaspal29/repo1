def main():
    infile = open('roster.txt', 'r')

    for line in infile:
        nameList = line.split()
        first = nameList[0]
        last = nameList[-1]
        newName = (f"{last},{first}")

    print(newName)

    infile.close()
main()


