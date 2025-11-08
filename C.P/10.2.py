def areBothEven(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return True
    return False

def main():
    numPairs = int(input("How many pairs? "))
    print()

    for i in range(numPairs):
        firstNum = int(input("Enter first number: "))
        secondNum = int(input("Enter second number: "))

    if firstNum % 2 == 0 and secondNum % 2 == 0:
            print(f"Sum is {firstNum + secondNum}")
            
        else:
            print(f"Product is {firstNum * secondNum}")
        print()
    
    
main()