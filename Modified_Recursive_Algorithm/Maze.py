
#       Author- Jacob Stringer
#       Date started - August 2019

from graphics import *
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
from tkinter import simpledialog
import pyautogui

#CheckValue is used by calling CheckValue.cV(sNi, flNi, value) and returns a
# string of the type of the value.

# sNi (string Not int) is a true false value that tells it whether or not this
# value needs to be checked as a string that will never have a number in it.

# flNi (float Not int) is a true false value that tells checkvalue whether to
# return float or int when the value's isinstance equals int. Because somtimes a
# float can be entered and evaluated as an int.



def checkMazeSize(mS):
    if 100 <= mS <= 800:
        #checks if the mazeSize is a usable value.
        mazeSizeRemainder = mS % 50
        #find how far from the next highest multiple of 50 we are.
        if mazeSizeRemainder > 0:
            #if the mazesize is not an exact multiple of 50, round it up to the
            #next highest multiple of 50
            mS = mS + (50 - mazeSizeRemainder)
        else:
            pass
    else:
        #if the maze Size is not a usable value, set it to zero so that it calls
        #a warning message and fails to draw.
        mS = 0

    return mS
# End of getMazeSize()

def checkHallSize(hS):
    #Checks if the mazesize is a usable value.

    if 0 < hS <= 50:
        if hS < 7:
            hS = 5
        elif hS < 17:
            hS = 10
        elif hS < 37:
            hS = 25
        else:
            hS = 50
    else:
        #if it is not a usable value, return -1 to call the warning message.
        hS = -1

    return hS
# End of getHallSize()

def createNewCells(mazeS, hallS):
    cellLs = []
    mH = mazeS / hallS
    mazeStart = (random.randint(0,(mH) - 1))
    mazeEnd = (random.randint(mH * mH - mH, (mH * mH) - 1))
    for i in range(0, int(mH * mH)):
        if i == mazeStart:
            cellLs.append(2)
        elif i == mazeEnd:
            cellLs.append(3)
        else:
            cellLs.append(0)
        #print(cellLs)
    return cellLs
# End of createNewCells()

def printM(win, m, h):
    maze_name = tkinter.simpledialog.askstring("Maze Title", "New Maze = ")
    time.sleep(.16)
    workingDir = os.getcwd()
    os.chdir(workingDir + "\\Mazes")
    x, y = win.windowInfo()
    im = pyautogui.screenshot(region=(x + 10, y + 75, m + 109, m + 25))
    name = "Maze_" + maze_name + "_" + str(m) + "x" + str(h) + ".png"
    im.save(name)
    os.chdir(workingDir)

def draw(mS2, hS2, cellLd, t, p):
    win = GraphWin("Maze Window", mS2 + 110, mS2 + 120)
    win.windowGeo(mS2 + 110, mS2 + 120, 50, 50)
    win.setBackground(color_rgb(255, 255, 255))
    rect = Rectangle(Point(54, 54), Point(mS2 + 56, mS2 + 56))
    rect.setFill(color_rgb(240, 240, 240))
    rect.setOutline(color_rgb(240, 240, 240))
    rect.draw(win)
    loadBarOutline = Rectangle(Point(54, mS2 + 90), Point(mS2 + 55, mS2 + 100))
    loadBarOutline.setFill(color_rgb(240, 240, 240))
    loadBarOutline.setOutline(color_rgb(0,0,0))
    loadBarOutline.draw(win)
    start = 0
    drawing_Msg = Text(Point(mS2/2 + 55, mS2 + 75), "Drawing...")
    drawing_Msg.draw(win)
    cellZ = int(mS2/hS2)
    nextCell = 0
    failLs = [0, 0, 0, 0]
    uCells =[]
    z = 0
    y = 55
    x = 55
    dir = 0
    fR = 0
    clear = 0
    l = 0

    for i in range(0, int(cellZ) + 1):
        grid = Line(Point(x,y), Point(x, mS2 + y))
        grid.setFill(color_rgb(0,0,0))
        grid.setWidth(2)
        grid.draw(win)
        x = x + hS2
    x = 55

    for i in range(0, int(cellZ) + 1):
        grid = Line(Point(x,y), Point(mS2 + x, y))
        grid.setFill(color_rgb(0,0,0))
        grid.setWidth(2)
        grid.draw(win)
        y = y + hS2
    y = 55

    for c in cellLd:
        if c == 2:
            cellLd[z] = 0
            start = z
            fc = Line(Point(x, y + (hS2 * z) + hS2 - 1), Point(x, y + (hS2 * z) + 1))
            fc.setFill(color_rgb(240, 240, 240))
            fc.setWidth(2)
            fc.draw(win)
            startMsg = Text(Point(x - 30, y + (hS2 * z) + hS2 - (hS2/2)), "Start->")
            startMsg.draw(win)

        elif c == 3:
            cCellx = math.floor(z/cellZ)
            if z > cellZ:
                cCelly = z - (cellZ * math.floor(z/cellZ))
            elif z == cellZ:
                cCelly = 0
            else:
                cCelly = cCell
            cellLd[z] = 0
            fc = Line(Point(x + (cCellx * hS2) + hS2, y + (hS2 * cCelly) + 1), Point(x + (cCellx * hS2) + hS2, y + (hS2 * cCelly) + hS2 - 1))
            fc.setFill(color_rgb(240, 240, 240))
            fc.setWidth(2)
            fc.draw(win)
            endMsg = Text(Point(x + (cCellx * hS2) + hS2 + 30, y + (hS2 * cCelly) + (hS2/2)), "<-End")
            endMsg.draw(win)

        else:
            pass
        z = z + 1

    loadbar = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
    loadbar.setFill(color_rgb(150, 150, 150))
    loadbar.draw(win)
    loadbar2 = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
    loadbar2.setFill(color_rgb(150, 150, 150))
    loadbar2.draw(win)
    loadbar2.undraw()

    nextCell = start + (cellZ)
    cellLd[start] = 1
    fc = Line(Point(x + hS2 , y + (hS2 * start) + 1), Point(x + hS2 ,y + (hS2 * start) + hS2 - 1))
    fc.setFill(color_rgb(240, 240, 240))
    fc.setWidth(2)
    fc.draw(win)
    time.sleep(.2)
    if l == 0:
        loadbar2 = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
        loadbar2.draw(win)
        loadbar.undraw()
        l = 1
    else:
        loadbar = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
        loadbar.draw(win)
        loadbar2.undraw()
        l = 0

    #print(cellLd.count(1), "/", cellZ * cellZ)
    #print(start, "-->", nextCell)
    cCell = nextCell
    cellLd[nextCell] = 1
    if l == 0:
        loadbar2 = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
        loadbar2.draw(win)
        loadbar.undraw()
        l = 1
    else:
        loadbar = Rectangle(Point(54, mS2 + 91), Point(((cellLd.count(1)/(cellZ ** 2)) * mS2) + 54, mS2 + 100))
        loadbar.draw(win)
        loadbar2.undraw()
        l = 0
    cCellx = 0
    cCelly = 0
    oneHallway = 0
    loadP = 55/22


    while 0 in cellLd:
        dir = random.randint(0,3)
        cCellx = math.floor(cCell/cellZ)
        if cCell > cellZ:
            cCelly = cCell - (cellZ * math.floor(cCell/cellZ))
        elif cCell == cellZ:
            cCelly = 0
        else:
            cCelly = cCell

        if dir == 0:
            nextCell = cCell - 1
            if nextCell > -1 and (cCell % cellZ) != 0 and cellLd[nextCell] == 0:
                wall = Line(Point(x + (cCellx * hS2) + 1, y + (hS2 * cCelly)), Point(x + (cCellx * hS2) + hS2 - 1, y + (hS2 * cCelly)))
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cellLd[nextCell] = 1
                loadP = cellLd.count(1)/(cellZ ** 2)
                if l == 0:
                    loadbar2 = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar2.draw(win)
                    loadbar.undraw()
                    l = 1
                else:
                    loadbar = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar.draw(win)
                    loadbar2.undraw()
                    l = 0
                #print(cCell, "-->", nextCell)
                uCells.append(cCell)
                cCell = nextCell
                if t == 1:
                    time.sleep(.08)

                if failLs.count(0) != 4:
                    failLs.clear()
                    for i in range(0,4):
                        failLs.append(0)
                oneHallway = oneHallway + 1
            else:
                failLs[0] = 1

        elif dir == 1:
            nextCell = cCell + cellZ
            if nextCell < (cellZ * cellZ) and cellLd[nextCell] == 0:
                wall = Line(Point(x + (cCellx * hS2) + hS2, y + (hS2 * cCelly) + 1), Point(x + (cCellx * hS2) + hS2, y + (hS2 * cCelly) + hS2 - 1))
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cellLd[nextCell] = 1
                loadP = cellLd.count(1)/(cellZ ** 2)
                if l == 0:
                    loadbar2 = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar2.draw(win)
                    loadbar.undraw()
                    l = 1
                else:
                    loadbar = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar.draw(win)
                    loadbar2.undraw()
                    l = 0
                #print(cCell, "-->", nextCell)
                uCells.append(cCell)
                cCell = nextCell
                if t == 1:
                    time.sleep(.08)

                if failLs.count(0) != 4:
                    failLs.clear()
                    for i in range(0,4):
                        failLs.append(0)
                oneHallway = oneHallway + 1
            else:
                failLs[1] = 1

        elif dir == 2:
            nextCell = cCell + 1
            if nextCell < (cellZ * cellZ) and ((cCell + 1) % cellZ) != 0 and cellLd[nextCell] == 0:
                wall = Line(Point(x + (cCellx * hS2) + hS2 - 1, y + (hS2 * cCelly) + hS2), Point(x + (cCellx * hS2) + 1, y + (hS2 * cCelly) + hS2))
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cellLd[nextCell] = 1
                loadP = cellLd.count(1)/(cellZ ** 2)
                if l == 0:
                    loadbar2 = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar2.draw(win)
                    loadbar.undraw()
                    l = 1
                else: #l can only be 0 or 1, hence when it is not 0 it is 1
                    loadbar = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar.draw(win)
                    loadbar2.undraw()
                    l = 0
                #print(cCell, "-->", nextCell)
                uCells.append(cCell)
                cCell = nextCell
                if t == 1:
                    time.sleep(.08)

                if failLs.count(0) != 4:
                    failLs.clear()
                    for i in range(0,4):
                        failLs.append(0)
                oneHallway = oneHallway + 1
            else:
                failLs[2] = 1

        elif dir == 3:
            nextCell = cCell - cellZ
            if nextCell > -1 and cellLd[nextCell] == 0:
                wall = Line(Point(x + (cCellx * hS2), y + (hS2 * cCelly) + hS2 - 1), Point(x + (cCellx * hS2), y + (hS2 * cCelly) + 1))
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cellLd[nextCell] = 1
                loadP = cellLd.count(1)/(cellZ ** 2)
                if l == 0:
                    loadbar2 = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar2.draw(win)
                    loadbar.undraw()
                    l = 1
                else:
                    loadbar = Rectangle(Point(54, mS2 + 91), Point((loadP * mS2) + 54, mS2 + 100))
                    loadbar.draw(win)
                    loadbar2.undraw()
                    l = 0
                #print(cCell, "-->", nextCell)
                uCells.append(cCell)
                cCell = nextCell
                if t == 1:
                    time.sleep(.08)

                if failLs.count(0) != 4:
                    failLs.clear()
                    for i in range(0,4):
                        failLs.append(0)
                oneHallway = oneHallway + 1
            else:
                failLs[3] = 1

        if (failLs.count(1) == 4) or (oneHallway == cellZ):
            randoCell = 0
            failLs.clear()
            if oneHallway == cellZ:
                #print("Long Hallway Check")
                fR = 3
                oneHallway = 0
            for i in range(0,4):
                failLs.append(0)
            if len(uCells) > 0:
                #print("Backtracking....")
                cCell = uCells.pop(len(uCells) - 1)
                #print(cellLd.count(1), "/", cellZ * cellZ)
                fR = fR + 1
            if fR == 4 and len(uCells) > 0:
                print("Current Stuck Cell: ", cCell)
                randoCell = random.randint(0, len(uCells) - 1)
                cCell = uCells.pop(randoCell)
                print("Random Used Cell: ", cCell)
                fR = 0
            if len(uCells) == 0:
                cCell = random.randint(0, (cellZ * cellZ) - 1)
    drawing_Msg.undraw()
    message = Text(Point(mS2/2 + 55, mS2 + 75), "Finished!")
    message.draw(win)
    g = 0
    if p.lower() == "yes":
        printM(win, mS2, hS2)
    if p.lower() == "yes":
        pass
    else:
        win.getMouse()
    win.close()
# End of draw()

def main():
    main = tkinter.Tk()
    mazeSizeStr = tkinter.StringVar()
    hallSizeStr = tkinter.StringVar()
    t = 0
    mainLabel = tkinter.Label(main, text="Modified Recursive Algorithm").grid(row=0, column=1, columnspan=1)
    mazeLabel = tkinter.Label(main, text="  Maze Size: ").grid(row=2, column=0)
    hallLabel = tkinter.Label(main, text="   Hall Size: ").grid(row=3, column=0)
    wtBLabel = tkinter.Label(main, text="   Watch Maze? ").grid(row=4, column=0)
    filler = tkinter.Label(main, text="                       |      ").grid(row=1, column=2)
    filler2 = tkinter.Label(main, text="(100-800)         |        ").grid(row=2, column=2)
    filler3 = tkinter.Label(main, text="(5/15/25/50)   |        ").grid(row=3, column=2)
    filler4 = tkinter.Label(main, text="(yes/no)          |        ").grid(row=4, column=2)
    fillerSide = tkinter.Label(main, text="          ").grid(row=0, column=4)
    fillerBottom = tkinter.Label(main, text="          ").grid(row=5, column=0)
    fillerTop = tkinter.Label(main, text="          ").grid(row=0, column=0)
    mazeSEntry = tkinter.Entry(main)
    hallSEntry = tkinter.Entry(main)
    wtB = tkinter.Entry(main)
    mazeSEntry.grid(row=2, column=1)
    hallSEntry.grid(row=3, column=1)
    wtB.grid(row=4, column=1)
    mazeSEntry.insert(0,'500')
    hallSEntry.insert(0,'25')
    wtB.insert(0,'no')


    def printIt():
        p = "yes"
        draws2(p)

    def draws():
        p = "no"
        draws2(p)

    def draws2(p):
        mazeSizeStr = mazeSEntry.get()
        hallSizeStr = hallSEntry.get()
        mazeSizec = stringToNumber.strToInt(mazeSizeStr)
        print(mazeSizec)
        hallSizec = stringToNumber.strToInt(hallSizeStr)
        print(hallSizec)
        mazeSize = checkMazeSize(mazeSizec)
        hallSize = checkHallSize(hallSizec)

        if mazeSize == 0:
            messagebox.showwarning("Invalid Maze Size Entry","Please enter a number between 100 and 800")
            return

        if hallSize == -1:
            messagebox.showwarning("Invalid Hall Size Entry","Please enter a number between 0 and 50")
            return

        if mazeSize < 200:
            if hallSize == 50:
                hallSize = 25
        cellList = []
        cellList = createNewCells(mazeSize, hallSize)
        print(cellList)
        if wtB.get().lower() == "yes":
            t = 1
        elif wtB.get().lower() == "no":
            t = 0
        elif wtB.get() == "":
            t = 0
        else:
            messagebox.showwarning("Invalid Entry","Please enter either yes or no")
            return

        if mazeSize/hallSize > mazeSize/4:
            t = 0
        else:
            pass
        print(t)
        main.iconify()
        draw(mazeSize, hallSize, cellList, t, p)
        main.deiconify()

    drawMaze = tkinter.Button(main, text="Draw Maze", command=draws)
    drawMaze.grid(row=2, column=3)
    printMaze = tkinter.Button(main, text="Print Maze", command=printIt)
    printMaze.grid(row=3, column=3)
    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=4, column=3)
    tkinter.mainloop()
# End of main()

if __name__ == '__main__':
    main()
