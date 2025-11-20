"""
 Name Rashmi Kaspal, date = 11/19/2025
 CSC 201
 Programming Project 2

 Description: This program begins with a gif image and creates a text file storing
              data for a "pointillistic" version of the image. The user can choose
              whether the background will be either white or black.

 Document Assistance: (who and what  OR  declare that you gave or received no assistance):
"""
from graphics2 import *
import random
import tkinter as tk
from tkinter import filedialog

NUM_CIRCLES = 7500
   
def main():
    #allows you to choose a file 
    root = tk.Tk()
    root.withdraw()
    filenameWithPath = filedialog.askopenfilename()
#    filenameWithPath = 'gallery/fall_retangular_scene.gif' # use this code if the file chooser doesn't work

    #add your code here
    if not filenameWithPath.endswith('.gif'):
        print("Invalid file format. Must choose a 'gif' file. ")
        print("Ending execution.")
        exit(-1)


    myImage = Image(Point(0,0), filenameWithPath)
    changeFile = filenameWithPath.split('.')
    artFile = changeFile[0] + '.art'
    fout = open(artFile, 'w')

    colorNum = int(input("Color for background? (1 white, 2 black) "))
    
    if colorNum == 1:
        color = 'white'
    elif colorNum == 2:
        color = 'black'
    else:
        color = 'white'
        colorNum = 1
        print("Invalid color choice. Using white")

    width = myImage.getWidth()
    height = myImage.getHeight()

    fout.write(f"{width} {height}\n")
    fout.write(f"{colorNum}\n")
    
    for index in range(NUM_CIRCLES):
        xCoordinate = random.randrange(width)
        yCoordinate = random.randrange(height)
        redNum, greenNum, blueNum = myImage.getPixel(xCoordinate, yCoordinate)
        radius = random.randrange(1, 10)
        fout.write(f"{redNum} {greenNum} {blueNum} {xCoordinate} {yCoordinate} {radius}\n")

    fout.close()

    artFileSplit = artFile.split('/')
    finalArtFile = artFileSplit[-1]
    print(f"File created: {finalArtFile}")
    print("Program ending.")


main()

#what didn't I do?
#didn't write almost anything to file
#didn't close the file 
# didn't kept just the file part but the whole location


