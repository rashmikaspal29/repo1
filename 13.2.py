import random
class SimpleSlotMachine:
    FRUIT_LIST = ['Lemon', 'Cherry', 'Apple', 'Orange', 'Banana', 'Raspberry',
                  'Peach', 'Watermelon', 'Kiwi', 'Grapes', 'Strawberry', 'Avocado',
                  'Plum', 'Pear', 'Lime', 'Pineapple', 'Fig', 'Honeydew',
                  'Blueberry','Papaya', 'Mango','Wild']

    PAY_OUT_WITH_WILD = 50
    PAY_OUT_SAME_FRUIT = 100
    PAY_OUT_ALL_WILD = 500
    
    def __init__(self):
        self._slot1 = random.choice(SimpleSlotMachine.FRUIT_LIST)
        self._slot2 = random.choice(SimpleSlotMachine.FRUIT_LIST)
        self._slot3 = random.choice(SimpleSlotMachine.FRUIT_LIST)
        self._payout = 0
        self._income = 0 

    def get_income(self):
        return (self._income)
    
    def get_total_payout(self):
        return self._payout
    
    def pull(self):
        self._slot1 = random.choice(SimpleSlotMachine.FRUIT_LIST)
        self._slot2 = random.choice(SimpleSlotMachine.FRUIT_LIST)
        self._slot3 = random.choice(SimpleSlotMachine.FRUIT_LIST)

        self._income = self._income + 1

    def get_payout(self):
        if self._slot1 == "Wild" and self._slot2 == "Wild" and self._slot3 == "Wild":
            player_payout = SimpleSlotMachine.PAY_OUT_WITH_WILD

        elif self._slot1 == self._slot2 and self._slot2 == self._slot3:
            player_payout = SimpleSlotMachine.PAY_OUT_SAME_FRUIT

        elif (self._slot1 == "Wild" and self._slot2 == self._slot3) or (self._slot2 == "Wild" and self._slot1 == self._slot3) or (self._slot3 == "Wild" and self._slot1 == self._slot2) or (self._slot1 =="Wild" and self._slot2 == "Wild") or (self._slot2 == "Wild" and self._slot3 == "Wild") or (self._slot3 == "Wild" and self._slot1 == "Wild"):
            player_payout = SimpleSlotMachine.PAY_OUT_WITH_WILD

        else:
            player_payout = 0

        self._payout = self._payout + player_payout

        return player_payout

    def __str__(self):
        return(f"{self._slot1} {self._slot2} {self._slot3}")
    

def main():
    random.seed(1234)
    machine1 = SimpleSlotMachine()
    print(machine1)

main()




