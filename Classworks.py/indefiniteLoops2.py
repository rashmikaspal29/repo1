def getValidResponse():
    response = input("Enter response: ")

    while response.lower() not in ['yes', 'no', 'y', 'n']:
        print("Invalid input. Try again.")
        response = input("Enter response: ")

    return response.lower()
    
def main():
    
    answer = getValidResponse()
    print(f'{answer} was returned.')

main()
    