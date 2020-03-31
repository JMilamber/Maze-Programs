#       Author- Jacob Stringer
#       Date started - November 18th 2019

import os
import tkinter
from tkinter import messagebox
import subprocess

try:
    import pyautogui
except ImportError:
    messagebox.showwarning(
        "Missing pyautogui",
        "Please install pyautogui via:\n\n " + "'pip install pyautogui'",
    )
    exit = 1
else:
    exit = 0


def main():
    main = tkinter.Tk()
    working_Dir = os.getcwd()

    def MRBA():
        directory_change = working_Dir + "/Randomized_Recursive_Backtracker"
        os.chdir(directory_change)
        subprocess.Popen(["RRBMaze.py"], shell=True)
        os.chdir(working_Dir)

    def RDA():
        directory_change = working_Dir + "/Recursive_Division"
        os.chdir(directory_change)
        subprocess.Popen(["RdMaze.py"], shell=True)
        os.chdir(working_Dir)

    def placeHolder1():
        pass

    def placeHolder2():
        pass

    mainLabel = tkinter.Label(main, text="Algorithm Selector").grid(
        row=1, column=2, columnspan=2
    )
    fillerMiddleTop = tkinter.Label(main, text="             ").grid(
        row=2, column=2, columnspan=2
    )
    fillerMiddleBottom = tkinter.Label(main, text="             ").grid(
        row=6, column=2, columnspan=2
    )
    fillerSide = tkinter.Label(main, text="             ").grid(row=7, column=7)
    fillerSide1 = tkinter.Label(main, text="                ").grid(
        row=0, column=0
    )
    ModifiedRecursiveAlgorithm = tkinter.Button(
        main,
        text="Randomized Recursive " + "Backtracker Algorithm",
        command=MRBA,
    )
    ModifiedRecursiveAlgorithm.grid(row=3, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(
        main, text="Recursive Division" + "Algorithm", command=RDA
    )
    ModifiedRecursiveAlgorithm.grid(row=4, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(
        main, text="_____ Algorithm", command=placeHolder1
    )
    ModifiedRecursiveAlgorithm.grid(row=5, column=2, columnspan=2)
    ModifiedRecursiveAlgorithm = tkinter.Button(
        main, text="_____ Algorithm", command=placeHolder2
    )

    ModifiedRecursiveAlgorithm.grid(row=6, column=2, columnspan=2)
    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=7, column=2, columnspan=2)
    tkinter.mainloop()


if __name__ == "__main__":
    if exit == 0:
        main()
    else:
        pass
