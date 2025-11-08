def main():
    maximum = float('-inf')
    number = input("Enter number (<Enter> to quit): ")

    while number != '':
        strNum = float(number)
        if strNum > maximum:
            maximum = strNum
        number = input("Enter number (<Enter> to quit): ")
    
    print()
    print(f"Maximum is {round(maximum, 2)}")
main()
        