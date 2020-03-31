#       Author- Jacob Stringer
#       Date started - August 2019

from graphics import *
import os
import random
import time
import math
import stringToNumber
import tkinter
from tkinter import messagebox
from tkinter import simpledialog

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

# CheckValue is used by calling CheckValue.cV(sNi, flNi, value) and returns a
# string of the type of the value.

# sNi (string Not int) is a true false value that tells it whether or not this
# value needs to be checked as a string that will never have a number in it.

# flNi (float Not int) is a true false value that tells checkvalue whether to
# return float or int when the value's isinstance equals int. Because somtimes
# a float can be entered and evaluated as an int.


def check_Maze_Size(m_S):
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
        # calls a warning message and fails to draw.
        m_S = 0

    return m_S


# End of getMazeSize()


def check_Hall_Size(h_S):
    # Checks if the mazesize is a usable value.

    if 0 < h_S <= 50:
        if h_S < 7:
            h_S = 5
        elif h_S < 17:
            h_S = 10
        elif h_S < 37:
            h_S = 25
        else:
            h_S = 50
    else:
        # if it is not a usable value, return -1 to call the warning message.
        h_S = -1

    return h_S


# End of getHallSize()


def create_New_Cells(mazeS, hallS):
    cell_Ls = []
    m_H = mazeS / hallS
    maze_Start = random.randint(0, (m_H) - 1)
    maze_End = random.randint(m_H * m_H - m_H, (m_H * m_H) - 1)
    for i in range(0, int(m_H * m_H)):
        if i == maze_Start:
            cell_Ls.append(2)
        elif i == maze_End:
            cell_Ls.append(3)
        else:
            cell_Ls.append(0)
        # print(cell_Ls)
    return cell_Ls


# End of create_New_Cells()


def Save_M(win, m, h):
    maze_name = tkinter.simpledialog.askstring("Maze Title", "New Maze = ")
    time.sleep(0.16)
    working_Dir = os.getcwd()
    os.chdir(working_Dir + "\\Mazes")
    x, y = win.windowInfo()
    im = pyautogui.screenshot(region=(x + 10, y + 75, m + 109, m + 25))
    name = "Maze_" + maze_name + "_" + str(m) + "x" + str(h) + ".png"
    im.save(name)
    os.chdir(working_Dir)


def draw(m_S_2, h_S_2, cell_Ld, t, p):
    win = GraphWin("Maze Window", m_S_2 + 110, m_S_2 + 120)
    win.windowGeo(m_S_2 + 110, m_S_2 + 120, 50, 50)
    win.setBackground(color_rgb(255, 255, 255))
    rect = Rectangle(Point(54, 54), Point(m_S_2 + 56, m_S_2 + 56))
    rect.setFill(color_rgb(240, 240, 240))
    rect.setOutline(color_rgb(240, 240, 240))
    rect.draw(win)
    load_Bar_Outline = Rectangle(
        Point(54, m_S_2 + 90), Point(m_S_2 + 55, m_S_2 + 100)
    )
    load_Bar_Outline.setFill(color_rgb(240, 240, 240))
    load_Bar_Outline.setOutline(color_rgb(0, 0, 0))
    load_Bar_Outline.draw(win)
    start = 0
    drawing_Msg = Text(Point(m_S_2 / 2 + 55, m_S_2 + 75), "Drawing...")
    drawing_Msg.draw(win)
    cell_Z = int(m_S_2 / h_S_2)
    next_Cell = 0
    fail_Ls = [0, 0, 0, 0]
    used_Cells = []
    z = 0
    y = 55
    x = 55
    dir = 0
    dead_end_count = 0
    load_bar_switch = 0

    for i in range(0, int(cell_Z) + 1):
        grid = Line(Point(x, y), Point(x, m_S_2 + y))
        grid.setFill(color_rgb(0, 0, 0))
        grid.setWidth(2)
        grid.draw(win)
        x = x + h_S_2
    x = 55

    for i in range(0, int(cell_Z) + 1):
        grid = Line(Point(x, y), Point(m_S_2 + x, y))
        grid.setFill(color_rgb(0, 0, 0))
        grid.setWidth(2)
        grid.draw(win)
        y = y + h_S_2
    y = 55

    for c in cell_Ld:
        if c == 2:
            cell_Ld[z] = 0
            start = z
            First_Line = Line(
                Point(x, y + (h_S_2 * z) + h_S_2 - 1),
                Point(x, y + (h_S_2 * z) + 1),
            )
            First_Line.setFill(color_rgb(240, 240, 240))
            First_Line.setWidth(2)
            First_Line.draw(win)
            start_Msg = Text(
                Point(x - 30, y + (h_S_2 * z) + h_S_2 - (h_S_2 / 2)), "Start->"
            )
            start_Msg.draw(win)

        elif c == 3:
            c_Cell_x = math.floor(z / cell_Z)
            if z > cell_Z:
                c_Cell_y = z - (cell_Z * math.floor(z / cell_Z))
            elif z == cell_Z:
                c_Cell_y = 0
            else:
                c_Cell_y = c_Cell
            cell_Ld[z] = 0
            Second_Line = Line(
                Point(
                    x + (c_Cell_x * h_S_2) + h_S_2, y + (h_S_2 * c_Cell_y) + 1
                ),
                Point(
                    x + (c_Cell_x * h_S_2) + h_S_2,
                    y + (h_S_2 * c_Cell_y) + h_S_2 - 1,
                ),
            )
            Second_Line.setFill(color_rgb(240, 240, 240))
            Second_Line.setWidth(2)
            Second_Line.draw(win)
            end_Msg = Text(
                Point(
                    x + (c_Cell_x * h_S_2) + h_S_2 + 30,
                    y + (h_S_2 * c_Cell_y) + (h_S_2 / 2),
                ),
                "<-End",
            )
            end_Msg.draw(win)

        else:
            pass
        z = z + 1

    load_bar = Rectangle(
        Point(54, m_S_2 + 91),
        Point(((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100),
    )
    load_bar.setFill(color_rgb(150, 150, 150))
    load_bar.draw(win)
    load_bar_2 = Rectangle(
        Point(54, m_S_2 + 91),
        Point(((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100),
    )
    load_bar_2.setFill(color_rgb(150, 150, 150))
    load_bar_2.draw(win)
    load_bar_2.undraw()

    next_Cell = start + (cell_Z)
    cell_Ld[start] = 1
    Third_Line = Line(
        Point(x + h_S_2, y + (h_S_2 * start) + 1),
        Point(x + h_S_2, y + (h_S_2 * start) + h_S_2 - 1),
    )
    Third_Line.setFill(color_rgb(240, 240, 240))
    Third_Line.setWidth(2)
    Third_Line.draw(win)
    time.sleep(0.2)
    if load_bar_switch == 0:
        load_bar_2 = Rectangle(
            Point(54, m_S_2 + 91),
            Point(
                ((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100
            ),
        )
        load_bar_2.draw(win)
        load_bar.undraw()
        load_bar_switch = 1
    else:
        load_bar = Rectangle(
            Point(54, m_S_2 + 91),
            Point(
                ((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100
            ),
        )
        load_bar.draw(win)
        load_bar_2.undraw()
        load_bar_switch = 0

    # print(cell_Ld.count(1), "/", cell_Z * cell_Z)
    # print(start, "-->", next_Cell)
    c_Cell = next_Cell
    cell_Ld[next_Cell] = 1
    if load_bar_switch == 0:
        load_bar_2 = Rectangle(
            Point(54, m_S_2 + 91),
            Point(
                ((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100
            ),
        )
        load_bar_2.draw(win)
        load_bar.undraw()
        load_bar_switch = 1
    else:
        load_bar = Rectangle(
            Point(54, m_S_2 + 91),
            Point(
                ((cell_Ld.count(1) / (cell_Z ** 2)) * m_S_2) + 54, m_S_2 + 100
            ),
        )
        load_bar.draw(win)
        load_bar_2.undraw()
        load_bar_switch = 0
    c_Cell_x = 0
    c_Cell_y = 0
    one_Hallway = 0
    load_Percent = 55 / 22

    while 0 in cell_Ld:
        dir = random.randint(0, 3)
        c_Cell_x = math.floor(c_Cell / cell_Z)
        if c_Cell > cell_Z:
            c_Cell_y = c_Cell - (cell_Z * math.floor(c_Cell / cell_Z))
        elif c_Cell == cell_Z:
            c_Cell_y = 0
        else:
            c_Cell_y = c_Cell

        if dir == 0:
            next_Cell = c_Cell - 1
            if (
                next_Cell > -1
                and (c_Cell % cell_Z) != 0
                and cell_Ld[next_Cell] == 0
            ):
                wall = Line(
                    Point(x + (c_Cell_x * h_S_2) + 1, y + (h_S_2 * c_Cell_y)),
                    Point(
                        x + (c_Cell_x * h_S_2) + h_S_2 - 1,
                        y + (h_S_2 * c_Cell_y),
                    ),
                )
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cell_Ld[next_Cell] = 1
                load_Percent = cell_Ld.count(1) / (cell_Z ** 2)
                if load_bar_switch == 0:
                    load_bar_2 = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar_2.draw(win)
                    load_bar.undraw()
                    load_bar_switch = 1
                else:
                    load_bar = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar.draw(win)
                    load_bar_2.undraw()
                    load_bar_switch = 0
                # print(c_Cell, "-->", next_Cell)
                used_Cells.append(c_Cell)
                c_Cell = next_Cell
                if t == 1:
                    time.sleep(0.08)

                if fail_Ls.count(0) != 4:
                    fail_Ls.clear()
                    for i in range(0, 4):
                        fail_Ls.append(0)
                one_Hallway = one_Hallway + 1
            else:
                fail_Ls[0] = 1

        elif dir == 1:
            next_Cell = c_Cell + cell_Z
            if next_Cell < (cell_Z * cell_Z) and cell_Ld[next_Cell] == 0:
                wall = Line(
                    Point(
                        x + (c_Cell_x * h_S_2) + h_S_2,
                        y + (h_S_2 * c_Cell_y) + 1,
                    ),
                    Point(
                        x + (c_Cell_x * h_S_2) + h_S_2,
                        y + (h_S_2 * c_Cell_y) + h_S_2 - 1,
                    ),
                )
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cell_Ld[next_Cell] = 1
                load_Percent = cell_Ld.count(1) / (cell_Z ** 2)
                if load_bar_switch == 0:
                    load_bar_2 = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar_2.draw(win)
                    load_bar.undraw()
                    load_bar_switch = 1
                else:
                    load_bar = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar.draw(win)
                    load_bar_2.undraw()
                    load_bar_switch = 0
                # print(c_Cell, "-->", next_Cell)
                used_Cells.append(c_Cell)
                c_Cell = next_Cell
                if t == 1:
                    time.sleep(0.08)

                if fail_Ls.count(0) != 4:
                    fail_Ls.clear()
                    for i in range(0, 4):
                        fail_Ls.append(0)
                one_Hallway = one_Hallway + 1
            else:
                fail_Ls[1] = 1

        elif dir == 2:
            next_Cell = c_Cell + 1
            if (
                next_Cell < (cell_Z * cell_Z)
                and ((c_Cell + 1) % cell_Z) != 0
                and cell_Ld[next_Cell] == 0
            ):
                wall = Line(
                    Point(
                        x + (c_Cell_x * h_S_2) + h_S_2 - 1,
                        y + (h_S_2 * c_Cell_y) + h_S_2,
                    ),
                    Point(
                        x + (c_Cell_x * h_S_2) + 1,
                        y + (h_S_2 * c_Cell_y) + h_S_2,
                    ),
                )
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cell_Ld[next_Cell] = 1
                load_Percent = cell_Ld.count(1) / (cell_Z ** 2)
                if load_bar_switch == 0:
                    load_bar_2 = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar_2.draw(win)
                    load_bar.undraw()
                    load_bar_switch = 1
                else:
                    # load_bar_switch can only be 0 or 1, hence when it is not
                    # 0 it is 1
                    load_bar = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar.draw(win)
                    load_bar_2.undraw()
                    load_bar_switch = 0
                # print(c_Cell, "-->", next_Cell)
                used_Cells.append(c_Cell)
                c_Cell = next_Cell
                if t == 1:
                    time.sleep(0.08)

                if fail_Ls.count(0) != 4:
                    fail_Ls.clear()
                    for i in range(0, 4):
                        fail_Ls.append(0)
                one_Hallway = one_Hallway + 1
            else:
                fail_Ls[2] = 1

        elif dir == 3:
            next_Cell = c_Cell - cell_Z
            if next_Cell > -1 and cell_Ld[next_Cell] == 0:
                wall = Line(
                    Point(
                        x + (c_Cell_x * h_S_2),
                        y + (h_S_2 * c_Cell_y) + h_S_2 - 1,
                    ),
                    Point(x + (c_Cell_x * h_S_2), y + (h_S_2 * c_Cell_y) + 1),
                )
                wall.setFill(color_rgb(240, 240, 240))
                wall.setWidth(2)
                wall.draw(win)
                cell_Ld[next_Cell] = 1
                load_Percent = cell_Ld.count(1) / (cell_Z ** 2)
                if load_bar_switch == 0:
                    load_bar_2 = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar_2.draw(win)
                    load_bar.undraw()
                    load_bar_switch = 1
                else:
                    load_bar = Rectangle(
                        Point(54, m_S_2 + 91),
                        Point((load_Percent * m_S_2) + 54, m_S_2 + 100),
                    )
                    load_bar.draw(win)
                    load_bar_2.undraw()
                    load_bar_switch = 0
                # print(c_Cell, "-->", next_Cell)
                used_Cells.append(c_Cell)
                c_Cell = next_Cell
                if t == 1:
                    time.sleep(0.08)

                if fail_Ls.count(0) != 4:
                    fail_Ls.clear()
                    for i in range(0, 4):
                        fail_Ls.append(0)
                one_Hallway = one_Hallway + 1
            else:
                fail_Ls[3] = 1

        if (fail_Ls.count(1) == 4) or (one_Hallway == cell_Z):
            rando_Cell = 0
            fail_Ls.clear()
            if one_Hallway == cell_Z:
                # print("Long Hallway Check")
                dead_end_count = 3
                one_Hallway = 0
            for i in range(0, 4):
                fail_Ls.append(0)
            if len(used_Cells) > 0:
                # print("Backtracking....")
                c_Cell = used_Cells.pop(len(used_Cells) - 1)
                # print(cell_Ld.count(1), "/", cell_Z * cell_Z)
                dead_end_count = dead_end_count + 1
            if dead_end_count == 4 and len(used_Cells) > 0:
                print("Current Stuck Cell: ", c_Cell)
                rando_Cell = random.randint(0, len(used_Cells) - 1)
                c_Cell = used_Cells.pop(rando_Cell)
                print("Random Used Cell: ", c_Cell)
                dead_end_count = 0
            if len(used_Cells) == 0:
                c_Cell = random.randint(0, (cell_Z * cell_Z) - 1)
    drawing_Msg.undraw()
    message = Text(Point(m_S_2 / 2 + 55, m_S_2 + 75), "Finished!")
    message.draw(win)
    if p.lower() == "yes":
        Save_M(win, m_S_2, h_S_2)
    if p.lower() == "yes":
        pass
    else:
        win.getMouse()
    win.close()


# End of draw()


def main():
    main = tkinter.Tk()
    maze_Size_Str = tkinter.StringVar()
    hall_Size_Str = tkinter.StringVar()
    main_Label = tkinter.Label(
        main, text="Modified Recursive" + " Algorithm"
    ).grid(row=0, column=1, columnspan=1)
    maze_Label = tkinter.Label(main, text="  Maze Size: ").grid(row=2, column=0)
    hall_Label = tkinter.Label(main, text="   Hall Size: ").grid(
        row=3, column=0
    )
    w_t_B_Label = tkinter.Label(main, text="   Watch Maze? ").grid(
        row=4, column=0
    )
    filler = tkinter.Label(
        main, text="               " + "        |      "
    ).grid(row=1, column=2)
    filler_2 = tkinter.Label(
        main, text="(100-800)    " + "     |        "
    ).grid(row=2, column=2)
    filler_3 = tkinter.Label(main, text="(5/15/25/50) " + "  |        ").grid(
        row=3, column=2
    )
    filler_4 = tkinter.Label(
        main, text="(yes/no)     " + "     |        "
    ).grid(row=4, column=2)
    filler_Side = tkinter.Label(main, text="          ").grid(row=0, column=4)
    filler_Bottom = tkinter.Label(main, text="          ").grid(row=5, column=0)
    filler_Top = tkinter.Label(main, text="          ").grid(row=0, column=0)
    maze_S_Entry = tkinter.Entry(main)
    hall_S_Entry = tkinter.Entry(main)
    w_t_B = tkinter.Entry(main)
    maze_S_Entry.grid(row=2, column=1)
    hall_S_Entry.grid(row=3, column=1)
    w_t_B.grid(row=4, column=1)
    maze_S_Entry.insert(0, "500")
    hall_S_Entry.insert(0, "25")
    w_t_B.insert(0, "no")

    def Save_It():
        p = "yes"
        C_draw(p)

    def D_Save_It():
        p = "no"
        C_draw(p)

    def C_draw(p):
        maze_Size_Str = maze_S_Entry.get()
        hall_Size_Str = hall_S_Entry.get()
        maze_Size_c = stringToNumber.strToInt(maze_Size_Str)
        print(maze_Size_c)
        hall_Size_c = stringToNumber.strToInt(hall_Size_Str)
        print(hall_Size_c)
        maze_Size = check_Maze_Size(maze_Size_c)
        hall_Size = check_Hall_Size(hall_Size_c)

        if maze_Size == 0:
            messagebox.showwarning(
                "Invalid Maze Size Entry",
                "Please enter a number between 100 and 800",
            )
            return

        if hall_Size == -1:
            messagebox.showwarning(
                "Invalid Hall Size Entry",
                "Please enter a number between 0 and 50",
            )
            return

        if maze_Size < 200:
            if hall_Size == 50:
                hall_Size = 25
        cell_List = []
        cell_List = create_New_Cells(maze_Size, hall_Size)
        print(cell_List)
        if w_t_B.get().lower() == "yes":
            t = 1
        elif w_t_B.get().lower() == "no":
            t = 0
        elif w_t_B.get() == "":
            t = 0
        else:
            messagebox.showwarning(
                "Invalid Entry", "Please enter either yes or no"
            )
            return

        if maze_Size / hall_Size > maze_Size / 4:
            t = 0
        else:
            pass
        print(t)
        main.iconify()
        draw(maze_Size, hall_Size, cell_List, t, p)
        main.deiconify()

    Draw_Maze = tkinter.Button(main, text="Draw Maze", command=D_Save_It)
    Draw_Maze.grid(row=2, column=3)
    Save_Maze = tkinter.Button(main, text="Save Maze", command=Save_It)
    Save_Maze.grid(row=3, column=3)
    quit = tkinter.Button(main, text="Quit", command=main.quit)
    quit.grid(row=4, column=3)
    tkinter.mainloop()


# End of main()


if __name__ == "__main__":
    if exit == 0:
        main()
    else:
        pass
