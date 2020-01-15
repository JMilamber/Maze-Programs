#       Author- Jacob Stringer
#       Date started - November 19th 2019

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


class Area:

    def __init__(self, x_initial, y_initial, width_initial, height_initial):
        self.x = x_initial
        self.y = y_initial
        self.width = width_initial
        self.height = height_initial
        self.isHall = 0

    def isH(self, hallS):
        # method to check whether thearea is the width of a single hall
        if (self.width == hallS) or (self.height == hallS):
            self.isHall = 1
        else:
            self.isHall = 0
        # 1 = True, 0 = False
        return self.isHall

    def size(self, mS):
        # method to check whether the area is a square or rectangle, and if it
        # is a rectangle, what its orientation is.
        if self.height > self.width:
            return self.height/mS
        elif self.width > self.height:
            return self.width/mS
        else:
            return ((self.height/mS) + (self.width/mS)) / 2

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


class Wall:

    def __init__(self, x11, y11, x12, y12):
        self.x = x11
        self.y = y11
        self.x1 = x12
        self.y1 = y12

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getX1(self):
        return self.x1

    def getY1(self):
        return self.y1

def printM(win, m, h):
    maze_name = tkinter.simpledialog.askstring("Maze Title", "New Maze = ")
    time.sleep(.25)
    workingDir = os.getcwd()
    os.chdir(workingDir + "\\Mazes")
    x, y = win.windowInfo()
    im = pyautogui.screenshot(region=(x + 10, y + 75, m + 109, m + 25))
    name = "Maze_" + maze_name + "_" + str(m) + "x" + str(h) + ".png"
    im.save(name)
    os.chdir(workingDir)

def checkMazeSize(mS):
    print("in check maze size")
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


def horizontalORveritcal(height, width):
    # Gets two parameters, the height and width of the area.
    hv = 0
    if height > width:
        hv = 0
    elif width > height:
        hv = 1
    else:
        hV = random.randint(0,1)
    return hv
# End of horizontalORveritcal()

def split(areaToSplit, hallS, hallArea_dict, id):
    x = areaToSplit.getX()
    y = areaToSplit.getY()
    height = areaToSplit.getHeight()
    width = areaToSplit.getWidth()
    hV = horizontalORveritcal(height, width)
    # Gets whether it should cut the area horizontally(0) or vertically (1)
    id = id + 1
    wallnum = 0
    walls = 0

    if hV == 0:
        # Horizontal
        walls = int(height/hallS)
        #print("# of H Walls in Area: ", walls - 1)
        # computes the number of walls in this area
        wallnum = random.randint(1, walls - 1)
        # picks a random wall from said number of walls to use
        hallArea_dict["0" + str(id)] = Area(x, y, width, wallnum * hallS)
        id = id + 1
        hallArea_dict["0" + str(id)] = Area(x, y + wallnum * hallS, width, height - wallnum * hallS)

    elif hV == 1:
        # Vertical
        walls = int(width/hallS)
        #print("# of V Walls in Area: ", walls - 1)
        # computes the number of walls in this area
        wallnum = random.randint(1, walls - 1)
        # picks a random wall from said number of walls to use
        hallArea_dict["0" + str(id)] = Area(x, y, wallnum * hallS, height)
        id = id + 1
        hallArea_dict["0" + str(id)] = Area(x + wallnum * hallS, y, width - wallnum * hallS, height)

    return hallArea_dict, hV, wallnum, id
    # returns the then changed hallArea_dict, whether it cut horizontally or
    # vertically, and which wall it chose to add
# End of split()

def pickNewArea(hallArea_dict, hallS, mazeS):
    smallest = 1.1
    areaKey = ""
    done = 0
    size = 0
    done_list = []
    values_list = hallArea_dict.values()
    done_list.clear()
    for key, value in hallArea_dict.items():
        #print("value size: ", value.size(mazeS))
        if (value.size(mazeS) < smallest) & (value.isH(hallS) == 0):
            areaKey = key
            smallest = value.size(mazeS)
        elif value.isH(hallS) == 1:
            done_list.append(value.isH(hallS))
            #print("Is Hall")
        else:
            pass
    #print(done_list)
    if len(done_list) == len(values_list):
        done = 1
    else:
        done = 0

    return areaKey, done
# End of pickNewArea()

def draw(mazeS, hallS, p):
    offset = int((hallS * 3)/ 2)
    # value used to create a border around the maze which is empty space.
    if offset < 50:
        offset = 50
        # ensures a big enoughoffset for the start and end text.
    win = GraphWin("Maze Window", mazeS + offset * 2, mazeS + offset * 2)
    # creates window
    win.windowGeo(mazeS + offset * 2,mazeS + offset * 2, 50, 50)
    # sets the location of the window
    win.setBackground(color_rgb(255, 255, 255))
    # sets the background to white
    rect = Rectangle(Point(offset, offset), Point(mazeS + offset, mazeS + offset))
    # creates a rectangle object that the maze will be drawn on.
    rect.setFill(color_rgb(240, 240, 240))
    # sets the color to just off-white
    rect.setOutline(color_rgb(0, 0, 0))
    # sets the outline color to black
    rect.setWidth(2)
    rect.draw(win)
    message = Text(Point(mazeS/2 + offset , mazeS + (offset * 2) - (offset/2)), "Calculating...")
    message.draw(win)
    #hallS = 25
    id = 0
    hallArea_dict = {}
    hallArea_dict["0" + str(id)] = Area(0, 0, mazeS, mazeS)
    #print(hallArea_dict)
    walls_list = []
    passage_list = []
    hv = 0
    done = 0
    wallToAdd = 0
    wallToRemove = 0
    key = ""


    mH = mazeS / hallS
    mazeStart = (random.randint(0,(mH) - 1))
    mazeEnd = (random.randint(0,(mH) - 1))

    fc = Line(Point(offset, offset + (hallS * mazeStart) + hallS - 1), Point(offset, offset + (hallS * mazeStart) + 1))
    fc.setFill(color_rgb(240, 240, 240))
    fc.setWidth(2)
    fc.draw(win)
    startMsg = Text(Point(offset/2, offset + (hallS * mazeStart) + (hallS/2)), "Start->")
    startMsg.draw(win)

    fc = Line(Point(offset + mazeS, offset + (hallS * mazeEnd) + 1), Point(offset + mazeS, offset + (hallS * mazeEnd) + hallS- 1))
    fc.setFill(color_rgb(240, 240, 240))
    fc.setWidth(2)
    fc.draw(win)
    endMsg = Text(Point(offset * 1.5 + mazeS , offset + (hallS * mazeEnd) + (hallS/2)), "<-End")
    endMsg.draw(win)

    while done == 0:
        # loop to draw maze
        wallToAdd = 0
        key, done = pickNewArea(hallArea_dict, hallS, mazeS)
        # picks the next area for the prgoram to split.
        # returns the key for the next area and a 0 or 1 for "done" I.e. whether
        # or not the maze has been bisected as much as possible.

        if done == 0:
            # checks if the Maze is "done" 0 is false 1 is true.

            areaToSplit = hallArea_dict.get(key)
            # sets "areaToSplit" equal to the object area that we want to split,
            # allowing us to easily call methods from the area class


            #print("Keys: ", hallArea_dict.keys())
            hallArea_dict, hv, wallnum, id = split(areaToSplit, hallS, hallArea_dict, id)
            # splits the rea, returning whether it was split horizontally or
            # veritcally(hv), the id of the wall that needs to be added, and
            # the id # so that it can continue to be incremented if we ever need
            # to iterate over the hallArea_dict for a specific area.

            del hallArea_dict[key]
            # deletes the area we just split.
            #print("Keys: ", hallArea_dict.keys())

            if hv == 0:
                # if a horizontal wall
                walls_list.append(Wall(areaToSplit.getX(), areaToSplit.getY() + (wallnum * hallS), areaToSplit.getX() + areaToSplit.getWidth(), areaToSplit.getY() + (wallnum * hallS)))
                #add the new wall to the wall list, which the program uses to draw the walls after creating all of them.
                wallToRemove = (random.randint(1, areaToSplit.getWidth()/hallS) - 1) * hallS
                #print("H Wall to remove: ", wallToRemove/hallS)
                passage_list.append(Wall(areaToSplit.getX() + wallToRemove + 1, areaToSplit.getY() + (wallnum * hallS), areaToSplit.getX() + wallToRemove + hallS - 1, areaToSplit.getY() + (wallnum * hallS)))

            elif hv == 1:
                # if a vertical wall
                walls_list.append(Wall(areaToSplit.getX() + (wallnum * hallS), areaToSplit.getY(), areaToSplit.getX() + (wallnum * hallS), areaToSplit.getY() + areaToSplit.getHeight()))
                #add the new wall to the wall list, which the program uses to draw the walls after creating all of them.
                wallToRemove = (random.randint(1, areaToSplit.getHeight()/hallS) - 1) * hallS
                #print("V Wall to remove: ", wallToRemove/hallS)
                passage_list.append(Wall(areaToSplit.getX() + (wallnum * hallS), areaToSplit.getY() + wallToRemove + 1, areaToSplit.getX() + (wallnum * hallS), areaToSplit.getY() + wallToRemove + hallS - 1))

            else:
                pass

            #print("Walls: \n", walls_list)
            #print("Passages: \n", passage_list)





        #end of if done == 0

        else:
            pass

    # End of while done == 0

    print("Escaped")

    message.undraw()
    message = Text(Point(mazeS/2 + offset , mazeS + (offset * 2) - (offset/2)), "Drawing...")
    message.draw(win)

    a = 0
    for f in range(0,len(walls_list)):
        # draws the maze
        W = walls_list[f]
        #if a < 3:
            #time.sleep(.5)
            #a = a + .5
        #if hallS == 10 and mazeS > 150:
            #pass
        #elif hallS == 25:
            #time.sleep(.05)
        #elif mazeS < 700 and hallS == 50:
            #time.sleep(.08)
        #elif mazeS > 650 and hallS != 50:
            #time.sleep(.3)
        wall = Line(Point(W.getX() + offset, W.getY() + offset), Point(W.getX1() + offset, W.getY1()+ offset))
        wall.setFill(color_rgb(0, 0, 0))
        wall.setWidth(2)
        wall.draw(win)

        P = passage_list[f]
        passage = Line(Point(P.getX() + offset, P.getY() + offset), Point(P.getX1() + offset, P.getY1()+ offset))
        passage.setFill(color_rgb(240, 240, 240))
        passage.setWidth(2)
        passage.draw(win)


    message.undraw()
    # draws a message indicating to the suer that the maze has finished
    message = Text(Point(mazeS/2 + offset , mazeS + (offset * 2) - (offset/2)), "Finished!")
    message.draw(win)

    if p.lower() == "yes":
        printM(win, mazeS, hallS)

    if p.lower() == "yes":
        pass
    else:
        win.getMouse()
    win.close()
# End of draw()

def main():
    # gui steup
    main = tkinter.Tk()
    mazeSizeStr = tkinter.StringVar()
    hallSizeStr = tkinter.StringVar()
    mainLabel = tkinter.Label(main, text="Recursive Division").grid(row=0, column=1, columnspan=1)
    mazeLabel = tkinter.Label(main, text=" Maze Size:").grid(row=2, column=0)
    hallLabel = tkinter.Label(main, text="   Hall Size: ").grid(row=3, column=0)
    filler = tkinter.Label(main, text="-----------------------------------------------------------------|").grid(row=1, column=0, columnspan=3)
    filler2 = tkinter.Label(main, text="                (100 - 800)                |     ").grid(row=2, column=2)
    filler3 = tkinter.Label(main, text="    (small, medium, or large)  |     ").grid(row=3, column=2)
    filler4 = tkinter.Label(main, text="-----------------------------------------------------------------|").grid(row=4, column=0, columnspan=3)
    fillerSide = tkinter.Label(main, text="          ").grid(row=0, column=4)
    fillerBottom = tkinter.Label(main, text="          ").grid(row=5, column=0)
    fillerTop = tkinter.Label(main, text="          ").grid(row=0, column=0)

    def printIt():
        p = "yes"
        draw2(p)

    def draws():
        p = "no"
        draw2(p)

    def draw2(p):
        #function to initiate calculating and drawing the maze.
        mazeSizeStr = mazeSEntry.get()
        mazeSizec = stringToNumber.strToInt(mazeSizeStr)

        hallSizeStr = hallSEntry.get()
        mazeSize = checkMazeSize(mazeSizec)

        if hallSizeStr.lower() == "small":
            hallSize = 10
        elif hallSizeStr.lower() == "medium":
            hallSize = 25
        elif hallSizeStr.lower() == "large":
            hallSize = 50
        else:
            messagebox.showwarning("Invalid Hall Size Entry","Please enter small, medium, or large")
            return

        if mazeSize == 0:
            messagebox.showwarning("Invalid Maze Size Entry","Please enter a number between 100 and 800")
            return

        print(mazeSize)
        print(hallSize)
        main.iconify()
        draw(mazeSize, hallSize, p)
        main.deiconify()

    mazeSEntry = tkinter.Entry(main)
    mazeSEntry.grid(row=2, column=1)
    hallSEntry = tkinter.Entry(main)
    hallSEntry.grid(row=3, column=1)
    mazeSEntry.insert(0,'500')
    hallSEntry.insert(0,'medium')

    drawMaze = tkinter.Button(main, text="Draw Maze", command=draws)
    drawMaze.grid(row=2, column=3)
    printMaze = tkinter.Button(main, text="Print Maze", command=printIt)
    printMaze.grid(row=3, column=3)

    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=4, column=3)
    tkinter.mainloop()
if __name__ == '__main__':
    main()
