"""
 Name 
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
    

main()