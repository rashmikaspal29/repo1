class Food:
    def __init__(self, name,price, vegStatus):
        self._name = name 
        self._price = price 
        self._vegStatus = vegStatus

    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def isVeg(self):
        return self._vegStatus
    
    def addBacon(self):
        self._name = self.getName() + " with bacon"
        self._price = self.getPrice() + 3
        self._vegStatus = False

    def getDescription(self):
        if self._vegStatus == True:
            return (f"{self._name}(V): ${self._price:.2f}")
        else: 
            return(f"{self._name}: ${self._price:.2f}")
        

def main():
    food1 = Food('eggplant parmigiana', 12.95, True)
    print(food1.getDescription())
main()
        
            
    

