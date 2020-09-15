#       Author- Jacob Stringer
#       Date started - September 2020

import os
import random
import time
import math
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from Modules import stringToNumber
from Modules.graphics import *

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


class Set:
    # defines a set of cells, made up of cells in multiple rows.
    # used exclusively for calculating the maze as all cells eventually end
    # up part of the same set
    def __init__(self, num_init, cell_init):
        self.number = num_init
        self.cells = {}
        self.cells[cell_init.get_Id()] = cell_init
        self.num_of_cells = 1

    def addCellToSet(self, cell):
        # lists start at id 0 so the number of cells != the id of the first cell
        # rather it == the id of the next cell
        self.num_of_cells = num_of_cells + 1
        self.cells[cell.get_Id()] = cell
        cell.set_Set(self)

    def isCellInSet(self, cell):
        try:
            cells.get(cell.get_Id())
        except Exception as e:  # noqa: F841
            return False
        return True


class Id:
    def __init__(self):
        self.id = 0

    def getId(self):
        return self.id

    def incrementId(self):
        self.id = self.id + 1


class Cell:
    def __init__(self, x_init, y_init, set_init):
        self.x = x_init
        self.y = y_init
        self.set
        self.Id = (x * 10) + y
        # walls in the list go as follows: top, right, bottom, left
        self.walls = []

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_Id(self):
        return self.Id

    def get_Set(self):
        return self.set

    def set_Set(self, new_set):
        self.set = new_set

    def addWall(self, wall, wall_num):
        self.walls[wall_num] = wall

    def getWall(self, wall_num):
        return self.walls[wall_num]


class Wall:
    def __init__(self, x_11, y_11, x_12, y_12):
        self.x = x_11
        self.y = y_11
        self.x_1 = x_12
        self.y_1 = y_12

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_X_1(self):
        return self.x_1

    def get_Y_1(self):
        return self.y_1


def SaveM(win, m, h):
    maze_name = tkinter.simpledialog.askstring("Maze Title", "New Maze = ")
    time.sleep(0.25)
    working_Dir = os.getcwd()
    os.chdir(working_Dir + "\\Mazes")
    x, y = win.windowInfo()
    im = pyautogui.screenshot(region=(x + 10, y + 75, m + 109, m + 25))
    name = "Maze_" + maze_name + "_" + str(m) + "x" + str(h) + ".png"
    im.save(name)
    os.chdir(working_Dir)


def checkMazeSize(m_S):
    print("in check maze size")
    if 100 <= m_S <= 800:
        # checks if the mazeSize is a usable value.
        maze_Size_Remainder = m_S % 50
        # find how far from the next highest multiple of 50 we are.
        if maze_Size_Remainder > 0:
            # if the mazesize is not an exact multiple of 50, round it up to
            # the next highest multiple of 50
            m_S = m_S + (50 - maze_Size_Remainder)
        else:
            pass
    else:
        # if the maze Size is not a usable value, set it to zero so that it
        # calls warning message and fails to draw.
        m_S = 0

    return m_S


# End of checkMazeSize()


def AddCellsToSets(cell_list, m_H, next_set_Id, set_list, row, hall_S):
    for i in range(0, m_H):
        cell = cell_list[i + ((row - 1) * m_h)]
        try:
            cell_Set = cell.get_Set()
        except Exception as e:  # noqa F841
            cell.set_Set(Set(next_set_Id.getId()))
            set_list[next_set_Id.getId()] = Set(next_set_Id.getId(), cell)
            next_set_Id.incrementId()
            cell_Set = cell.get_Set()

    ConnectSetsInRow(cell_list, m_H, set_list, row, hall_S)


def ConnectSetsInRow(cell_list, m_H, set_list, row):
    for i in raneg(0, m_H):
        # 8 - i below so that we start on the right side of the row and merge
        cellBase = cell_list[8 - i + (row - 1) * m_h]
        cellCheck = cell_list[8 - i + ((row - 1) * m_h) - 1]
        if cellBase.get_Set() != cellCheck.get_Set():
            do_or_dont = ["do", "dont"]
            choice = random.choice(do_or_dont)
            if choice == "do":
                cellBase.addWall(
                    Wall(
                        cellBase.get_X(),
                        cellBase.get_Y(),
                        cellBase.get_X() + 1,
                        cellBase.get_Y(),
                    )
                )


def draw(maze_S, hall_S, p):
    offset = int((hall_S * 3) / 2)
    # value used to create a border around the maze which is empty space.
    if offset < 50:
        offset = 50
        # ensures a big enoughoffset for the start and end text.
    win = GraphWin("Maze Window", maze_S + offset * 2, maze_S + offset * 2)
    # creates window
    win.windowGeo(maze_S + offset * 2, maze_S + offset * 2, 50, 50)
    # sets the location of the window
    win.setBackground(color_rgb(255, 255, 255))
    # sets the background to white
    rect = Rectangle(
        Point(offset, offset), Point(maze_S + offset, maze_S + offset)
    )
    # creates a rectangle object that the maze will be drawn on.
    rect.setFill(color_rgb(240, 240, 240))
    # sets the color to just off-white
    rect.setOutline(color_rgb(0, 0, 0))
    # sets the outline color to black
    rect.setWidth(2)
    rect.draw(win)
    message = Text(
        Point(maze_S / 2 + offset, maze_S + (offset * 2) - (offset / 2)),
        "Calculating...",
    )

    message.draw(win)

    walls_list = []
    cell_list = []
    set_list = []
    m_H = maze_S / hall_S
    maze_Start = random.randint(0, (m_H) - 1)
    maze_End = random.randint(0, (m_H) - 1)
    next_set_Id = Id()
    x = 0
    y = 0

    for i in range(m_H * m_H):
        cell_list.append(Cell(x, y, -1))
        x = x + 1
        if x == m_H:
            y = y + 1
            x = 0

    AddCellRowToSets(cell_list, m_H, next_set_Id, set_list, 1, hall_S)

    # while (cell_list.length > 0):

    start = Line(
        Point(offset, offset + (hall_S * maze_Start) + hall_S - 1),
        Point(offset, offset + (hall_S * maze_Start) + 1),
    )
    start.setFill(color_rgb(240, 240, 240))
    start.setWidth(2)
    start.draw(win)
    start_Msg = Text(
        Point(offset / 2, offset + (hall_S * maze_Start) + (hall_S / 2)),
        "Start->",
    )
    start_Msg.draw(win)

    end = Line(
        Point(offset + maze_S, offset + (hall_S * maze_End) + 1),
        Point(offset + maze_S, offset + (hall_S * maze_End) + hall_S - 1),
    )
    end.setFill(color_rgb(240, 240, 240))
    end.setWidth(2)
    end.draw(win)
    end_Msg = Text(
        Point(
            offset * 1.5 + maze_S, offset + (hall_S * maze_End) + (hall_S / 2)
        ),
        "<-End",
    )
    end_Msg.draw(win)

    message.undraw()
    message = Text(
        Point(maze_S / 2 + offset, maze_S + (offset * 2) - (offset / 2)),
        "Drawing...",
    )
    message.draw(win)
    # maze code goes here.

    message.undraw()
    # draws a message indicating to the suer that the maze has finished
    message = Text(
        Point(maze_S / 2 + offset, maze_S + (offset * 2) - (offset / 2)),
        "Finished!",
    )
    message.draw(win)
    if p.lower() == "yes":
        SaveM(win, maze_S, hall_S)

    if p.lower() == "yes":
        pass
    else:
        win.getMouse()
    win.close()

    # End of draw()


def main():
    # gui steup
    main = tkinter.Tk()
    maze_Size_Str = tkinter.StringVar()
    hall_Size_Str = tkinter.StringVar()
    main_Label = tkinter.Label(main, text="Eller's Algorithim").grid(
        row=0, column=1, columnspan=1
    )
    maze_Label = tkinter.Label(main, text=" Maze Size:").grid(row=2, column=0)
    hall_Label = tkinter.Label(main, text="   Hall Size: ").grid(
        row=3, column=0
    )
    filler = tkinter.Label(
        main,
        text="-------------------------------------"
        + "----------------------------|",
    ).grid(row=1, column=0, columnspan=3)
    filler_2 = tkinter.Label(
        main, text="                (100 - 800)        " + "        |     "
    ).grid(row=2, column=2)
    filler_3 = tkinter.Label(
        main, text="    (small, medium, or large)  |   " + "  "
    ).grid(row=3, column=2)
    filler_4 = tkinter.Label(
        main,
        text="-----------------------------------------"
        + "------------------------|",
    ).grid(row=4, column=0, columnspan=3)
    filler_Side = tkinter.Label(main, text="          ").grid(row=0, column=4)
    filler_Bottom = tkinter.Label(main, text="          ").grid(row=5, column=0)
    filler_Top = tkinter.Label(main, text="          ").grid(row=0, column=0)

    def Save_It():
        p = "yes"
        C_draw(p)

    def D_Save_It():
        p = "no"
        C_draw(p)

    def C_draw(p):
        # function to initiate calculating and drawing the maze.
        maze_Size_Str = maze_S_Entry.get()
        maze_Size_c = stringToNumber.strToInt(maze_Size_Str)

        hall_Size_Str = hall_S_Entry.get()
        maze_Size = checkMazeSize(maze_Size_c)

        if hall_Size_Str.lower() == "small":
            hall_Size = 10
        elif hall_Size_Str.lower() == "medium":
            hall_Size = 25
        elif hall_Size_Str.lower() == "large":
            hall_Size = 50
        else:
            messagebox.showwarning(
                "Invalid Hall Size Entry",
                "Please enter small, medium, or large",
            )
            return

        if maze_Size == 0:
            messagebox.showwarning(
                "Invalid Maze Size Entry",
                "Please enter a number between 100 and 800",
            )
            return

        print(maze_Size)
        print(hall_Size)
        main.iconify()
        draw(maze_Size, hall_Size, p)
        main.deiconify()

    maze_S_Entry = tkinter.Entry(main)
    maze_S_Entry.grid(row=2, column=1)
    hall_S_Entry = tkinter.Entry(main)
    hall_S_Entry.grid(row=3, column=1)
    maze_S_Entry.insert(0, "500")
    hall_S_Entry.insert(0, "medium")

    draw_Maze = tkinter.Button(main, text="Draw Maze", command=D_Save_It)
    draw_Maze.grid(row=2, column=3)
    Save_Maze = tkinter.Button(main, text="Save Maze", command=Save_It)
    Save_Maze.grid(row=3, column=3)

    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=4, column=3)
    tkinter.mainloop()


# end of main


if __name__ == "__main__":
    if exit == 0:
        main()
    else:
        pass
