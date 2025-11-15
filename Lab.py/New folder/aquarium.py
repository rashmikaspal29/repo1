'''
Name(s): Rashmi Kaspal, Amira Babagana
CSC 201
Lab 8

The program displays a virtual aquarium with animated fish and floating bubbles.
It utilizes a Fish and Bubble class.

Did you complete this lab file during the class period (yes or no)?

If no, leave the one that applies. If yes, delete this entire section!
    I completed aquarium.py without my partner from class.
    I completed aquarium_game.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
'''


from graphics2 import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25
MAX_COLOR_NUM = 255
W = 60
H = 40
W1 = 10
H1 = 60
PIX = 20

#***********
# FISH CLASS
#***********

class Fish:
    def __init__(self, x, y, color, speed):
        self._body = Oval(Point(x-W/2, y-H/2), Point(x + W/2, y+H/2))
        self._tail = Oval(Point(x-PIX-W1/2, y-H1/2), Point(x-PIX+W1/2, y+H1/2))
        self._eye = Circle(Point(x+W/4, y-H/4), 3)
        self._speed = speed
        
    def draw(self, window):
        self._body.draw(window)
        self._tail.draw(window)
        self._eye.draw(window)

    def move(self):
        self._tail.move(self._speed, 0)
        x_cor1 = self._tail.getCenter().getX()
        
        if x_cor1 > 0:
            self._tail.move(WINDOW_WIDTH, 0)


        self._body.move(self._speed, 0)
        x_cor2 = self._body.getCenter().getX()
        
        if x_cor2 > 0:
            self._body.move(WINDOW_WIDTH, 0)


        self._eye.move(self._speed, 0)
        x_cor = self._eye.getCenter().getX()
        
        if x_cor > 0:
            self._eye.move(WINDOW_WIDTH, 0)


    

    
#*************
# BUBBLE CLASS
#*************

class Bubble:
    def __init__(self, x, y, speed):
        self._circle = Circle(Point(x,y), 5)
        self._circle.setFill("white")
        self._speed = speed
        
    def draw(self, window):
        self._circle.draw(window)
        
    def move(self):
        self._circle.move(0, self._speed)
        y_cor = self._circle.getCenter().getY()
        if y_cor < 0:
            self._circle.move(0, WINDOW_HEIGHT)
            
            
        
        
        

#*****************
# HELPER FUNCTIONS
#*****************

def setupInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
        win (GraphWin): the window the Entry box and label with be drawn in.
        point (Point): the location od the center of the text label
        text (str): the words that will be used to label the Entry box
    
    Returns:
        Entry: the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
        win (GraphWin): the window the Entry box is in
    
    Returns:
        (int, int): the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setupInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setupInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    
    Returns:
        Color: a random color
    '''
    red = random.randrange(0,MAX_COLOR_NUM + 1)
    green = random.randrange(0,MAX_COLOR_NUM + 1)
    blue = random.randrange(0,MAX_COLOR_NUM + 1)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
        numFish (int): the number of fish to be added to the list
    
    Returns:
        list: the list of fish
    '''
    fishList = []

    for index in range(numFish):
        x2 = random.randrange(0, WINDOW_WIDTH)
        y2 = random.randrange(0, WINDOW_HEIGHT)
        speed2 = random.randrange(1,6)
        color1 = randColor()
        fish = Fish(x2, y2, color1, speed2)
        fishList.append(fish)
    return fishList
        



def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed
    
    Params:
        numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
        list: the list of bubbbles
    '''
    bubbleList = []
    
    
    for index in range(numBubbles):
        x1 = random.randrange(0, WINDOW_WIDTH)
        y1 = random.randrange(0, WINDOW_HEIGHT)
        speed1 = random.randrange(-5, 0)
        bubble = Bubble(x1, y1, speed1)
        bubbleList.append(bubble)
    return bubbleList
        

#*****
# MAIN
#*****
def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")
    
    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    bubbleList = setupBubbles(numBubbles)
    fishList = setupFish(numFish)

    
    
    
    # draw the fish and bubbles in their initial locations
    for index in range(len(bubbleList)):
        bubbleList[index].draw(win)

    for index in range(len(fishList)):
        fishList[index].draw(win)
        
        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish calling move method on each fish
        for index in range(len(fishList)):
            fishList[index].move()


        # loop through all the bubbles calling move method on each bubble
        # The bubble are after the fish so that the bubbles are drawn in front of the fish
        for index in range(len(bubbleList)):
            bubbleList[index].move()
        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()

