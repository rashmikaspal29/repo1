def isLegal(age):
    if age >= 21:
        return True
    return False

def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print()
    
    if age >= 21:
        print(f"{name} is legal!")
    else:
        print(f"{name} is too young.")
main()
