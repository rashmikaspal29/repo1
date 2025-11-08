 def isValidResponse(response):
    listt = ['yes', 'y', 'no', 'n']
    
    if response.lower() not in listt:
        return False
     
    return True