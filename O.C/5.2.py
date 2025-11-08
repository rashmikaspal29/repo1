def doSquirrelsPlay(numTemp, isSummer):
    if isSummer:
        if numTemp >= 50 and numTemp <= 90:
            return True
        return False
    else:
        if numTemp >= 50 and numTemp <= 80:
            return True 
        else: 
            return False
 
def main():
    print(doSquirrelsPlay(81, False))
main()