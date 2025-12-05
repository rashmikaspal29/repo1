def getSeniorList(seniorDict):
    seniorList = []
    for senior in seniorDict.values():
        if senior >= 65:
            seniorList.append(senior)
            return seniorList.sort()
        else:
            return None
def main():
    getSeniorList({'Tom':27, 'Xue':17, 'Joe': 38, 'Al':64})
main()

