"""
 Name Rashmi Kaspal
 CSC 201
 Programming Project 2
 
 Description: This program reads a text file with an art extension and draws
              the "pointillistic" version of an image from the data in the file.
              The largest dimension is specified and the smaller dimension set
              proportionally.   
     
 Document Assistance: (who and what  OR  declare that you gave or received no assistance):
"""
from graphics2 import *
import tkinter as tk
from tkinter import filedialog

MAX_WINDOW_DIMENSION = 500

def main():
    #allows you to choose a file
    root = tk.Tk()
    root.withdraw()
    artFileName = filedialog.askopenfilename()
#    artFileName = 'gallery/fall_retangular_scene.art' # use this code if the file chooser doesn't work
    
    #add your code here
    if not artFileName.endswith('.art'):
        print("Invalid file format. Must choose an 'art' file.")
        print("Ending execution.")
        exit(-1)

    #open and read the artFile or a graphWin window
    fin = open(artFileName, 'r')

    firstLine = fin.readline().split()
    width = int(firstLine[0])
    height = int(firstLine[-1])

    secondLine = fin.readline()
    bgNum = int(secondLine[0])

    #scaling the window 
    if width > height:
        scale = MAX_WINDOW_DIMENSION/width
        newWidth = MAX_WINDOW_DIMENSION
        newHeight = int(height * scale)

    else:
        scale = MAX_WINDOW_DIMENSION/height
        newWidth = int(width * scale)
        newHeight = MAX_WINDOW_DIMENSION

    
    #for background color:
    if bgNum == 1:
        bgColor = 'white'
    else:
        bgColor = 'black'

    
    #creating a window:
    win = GraphWin("Art File" , newWidth, newHeight)
    win.setBackground(bgColor)


    #making for loop for 7500 circles:
    for line in fin:
        line = line.split() #split it before indexing as line is a string until you split it up
        red = int(line[0])
        green = int(line[1])
        blue = int(line[2])
        xCoordinate = int(line[3]) * scale # scale is already an integer not extracted from somewhere so
        yCoordinate = int(line[4]) * scale # so do not int that or the constant
        radius = int(line[5])

        color = color_rgb(red, green, blue) #store in a variable for future use

        #making a circle:
        circle = Circle(Point(xCoordinate, yCoordinate), radius)
        circle.setFill(color)
        circle.setOutline(color)
        circle.draw(win)

      
    fin.close()
    win.getMouse()
    print("Picture Completed.")
    

main()

#what I missed?
#all the ints
#variable mistake in secondLine
#int from the start 
#constant incorrect
#kept elif instead of else
#didn't added apostrophe in window at art file
#KEPT BGNUM INSTEAD OF BGCOLOR(BLUNDERRR)
#started indexing without spliting??



#major confusions or weak points
#xCoordinate 
#color_rgb thing

#minor:
#miskaten opening window and file 
# fumbled during reading file part
# x, y scaling part
#creating window part

#DO AGAIN. IMPROVEMENT NOT SHOWN


