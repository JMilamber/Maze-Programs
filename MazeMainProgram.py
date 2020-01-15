#       Author- Jacob Stringer
#       Date started - November 18th 2019

import os
import random
import time
import math
import CheckValue
import stringToNumber
import tkinter
from tkinter import constants
from tkinter import ttk
from tkinter import messagebox
import subprocess

def main():
    main = tkinter.Tk()
    workingDir = os.getcwd()
    def MRBA():
        os.chdir(r"D:\My Python Programming\MazeInPython\Modified_Recursive_Algorithm")
        subprocess.Popen(['Maze.py'], shell=True)
        os.chdir(workingDir)

    def RDA():
        os.chdir(r"D:\My Python Programming\MazeInPython\Recursive_Division")
        subprocess.Popen(['RdMaze.py'], shell=True)
        os.chdir(workingDir)

    def placeHolder1():
        pass

    def placeHolder2():
        pass

    mainLabel = tkinter.Label(main, text="Algorithm Selector").grid(row=1, column=2, columnspan=2)
    fillerMiddleTop = tkinter.Label(main, text="             ").grid(row=2, column=2, columnspan=2)
    fillerMiddleBottom = tkinter.Label(main, text="             ").grid(row=6, column=2, columnspan=2)
    fillerSide = tkinter.Label(main, text="             ").grid(row=7, column=7)
    fillerSide1 = tkinter.Label(main, text="                ").grid(row=0, column=0)
    ModifiedRecursiveAlgorithm = tkinter.Button(main, text="Modified Recursive Backtracker Algorithm", command=MRBA)
    ModifiedRecursiveAlgorithm.grid(row=3, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(main, text="Recursive Division Algorithm", command=RDA)
    ModifiedRecursiveAlgorithm.grid(row=4, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(main, text="_____ Algorithm", command=placeHolder1)
    ModifiedRecursiveAlgorithm.grid(row=5, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(main, text="_____ Algorithm", command=placeHolder2)
    ModifiedRecursiveAlgorithm.grid(row=6, column=2, columnspan=2)
    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=7, column=2, columnspan=2)
    tkinter.mainloop()





if __name__ == '__main__':
    main()
