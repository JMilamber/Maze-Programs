#       Author- Jacob Stringer
#       Date started - November 19th 2019

import os
import random
import time
from Modules import stringToNumber
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from Recursive_Division.Modules.graphics import *

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


class Area:
    def __init__(self, x_initial, y_initial, width_initial, height_initial):
        self.x = x_initial
        self.y = y_initial
        self.width = width_initial
        self.height = height_initial
        self.is_Hall = 0

    def is_H(self, hall_S):
        # method to check whether thearea is the width of a single hall
        if (self.width == hall_S) or (self.height == hall_S):
            self.is_Hall = 1
        else:
            self.is_Hall = 0
        # 1 = True, 0 = False
        return self.is_Hall

    def size(self, m_S):
        # method to check whether the area is a square or rectangle, and if it
        # is a rectangle, what its orientation is.
        if self.height > self.width:
            return self.height / m_S
        elif self.width > self.height:
            return self.width / m_S
        else:
            return ((self.height / m_S) + (self.width / m_S)) / 2

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_Width(self):
        return self.width

    def get_Height(self):
        return self.height


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


def Save_M(win, m, h):
    maze_name = tkinter.simpledialog.askstring("Maze Title", "New Maze = ")
    time.sleep(0.25)
    working_Dir = os.getcwd()
    os.chdir(working_Dir + "\\Mazes")
    x, y = win.windowInfo()
    im = pyautogui.screenshot(region=(x + 10, y + 75, m + 109, m + 25))
    name = "Maze_" + maze_name + "_" + str(m) + "x" + str(h) + ".png"
    im.save(name)
    os.chdir(working_Dir)


def check_Maze_Size(m_S):
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


# End of getMazeSize()


def horizontal_OR_veritcal(height, width):
    # Gets two parameters, the height and width of the area.
    h_V = 0
    if height > width:
        h_V = 0
    elif width > height:
        h_V = 1
    else:
        h_V = random.randint(0, 1)

    return h_V


# End of horizontal_OR_veritcal()


def split(area_To_Split, hall_S, hall_Area_dict, id):
    x = area_To_Split.get_X()
    y = area_To_Split.get_Y()
    height = area_To_Split.get_Height()
    width = area_To_Split.get_Width()
    h_V = horizontal_OR_veritcal(height, width)
    # Gets whether it should cut the area horizontally(0) or vertically (1)
    id = id + 1
    wall_num = 0
    walls = 0

    if h_V == 0:
        # Horizontal
        walls = int(height / hall_S)
        # print("# of H Walls in Area: ", walls - 1)
        # computes the number of walls in this area
        wall_num = random.randint(1, walls - 1)
        # picks a random wall from said number of walls to use
        hall_Area_dict["0" + str(id)] = Area(x, y, width, wall_num * hall_S)
        id = id + 1
        hall_Area_dict["0" + str(id)] = Area(
            x, y + wall_num * hall_S, width, height - wall_num * hall_S
        )

    elif h_V == 1:
        # Vertical
        walls = int(width / hall_S)
        # print("# of V Walls in Area: ", walls - 1)
        # computes the number of walls in this area
        wall_num = random.randint(1, walls - 1)
        # picks a random wall from said number of walls to use
        hall_Area_dict["0" + str(id)] = Area(x, y, wall_num * hall_S, height)
        id = id + 1
        hall_Area_dict["0" + str(id)] = Area(
            x + wall_num * hall_S, y, width - wall_num * hall_S, height
        )

    return hall_Area_dict, h_V, wall_num, id
    # returns the then changed hall_Area_dict, whether it cut horizontally or
    # vertically, and which wall it chose to add


# End of split()


def pick_New_Area(hall_Area_dict, hall_S, maze_S):
    smallest = 1.1
    area_Key = ""
    done = 0
    size = 0
    done_list = []
    values_list = hall_Area_dict.values()
    done_list.clear()
    for key, value in hall_Area_dict.items():
        # print("value size: ", value.size(maze_S))
        if (value.size(maze_S) < smallest) & (value.is_H(hall_S) == 0):
            area_Key = key
            smallest = value.size(maze_S)
        elif value.is_H(hall_S) == 1:
            done_list.append(value.is_H(hall_S))
            # print("Is Hall")
        else:
            pass
    # print(done_list)
    if len(done_list) == len(values_list):
        done = 1
    else:
        done = 0

    return area_Key, done


# End of pick_New_Area()


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
    # hall_S = 25
    id = 0
    hall_Area_dict = {}
    hall_Area_dict["0" + str(id)] = Area(0, 0, maze_S, maze_S)
    # print(hall_Area_dict)
    walls_list = []
    passage_list = []
    h_V = 0
    done = 0
    wall_To_Remove = 0
    key = ""

    m_H = maze_S / hall_S
    maze_Start = random.randint(0, (m_H) - 1)
    maze_End = random.randint(0, (m_H) - 1)

    first_Line = Line(
        Point(offset, offset + (hall_S * maze_Start) + hall_S - 1),
        Point(offset, offset + (hall_S * maze_Start) + 1),
    )
    first_Line.setFill(color_rgb(240, 240, 240))
    first_Line.setWidth(2)
    first_Line.draw(win)
    start_Msg = Text(
        Point(offset / 2, offset + (hall_S * maze_Start) + (hall_S / 2)),
        "Start->",
    )
    start_Msg.draw(win)

    first_Line = Line(
        Point(offset + maze_S, offset + (hall_S * maze_End) + 1),
        Point(offset + maze_S, offset + (hall_S * maze_End) + hall_S - 1),
    )
    first_Line.setFill(color_rgb(240, 240, 240))
    first_Line.setWidth(2)
    first_Line.draw(win)
    end_Msg = Text(
        Point(
            offset * 1.5 + maze_S, offset + (hall_S * maze_End) + (hall_S / 2)
        ),
        "<-End",
    )
    end_Msg.draw(win)

    while done == 0:
        # loop to draw maze

        key, done = pick_New_Area(hall_Area_dict, hall_S, maze_S)
        # picks the next area for the prgoram to split.
        # returns the key for the next area and 0 or 1 for "done".
        # I.e. whether or not the maze has been bisected as much as possible.

        if done == 0:
            # checks if the Maze is "done" 0 is false 1 is true.

            area_To_Split = hall_Area_dict.get(key)
            # sets "area_To_Split" equal to the object area that we want to
            # split, allowing us to easily call methods from the area class

            # print("Keys: ", hall_Area_dict.keys())
            hall_Area_dict, h_V, wall_num, id = split(
                area_To_Split, hall_S, hall_Area_dict, id
            )
            # splits the area returning: whether it was split horizontally or
            # veritcally(h_V), the id of the wall that needs to be added, and
            # the id # so that it can continue to be incremented if we need
            # to iterate over the hall_Area_dict for a specific area.

            del hall_Area_dict[key]
            # deletes the area we just split.
            # print("Keys: ", hall_Area_dict.keys())

            if h_V == 0:
                # if a horizontal wall
                walls_list.append(
                    Wall(
                        area_To_Split.get_X(),
                        area_To_Split.get_Y() + (wall_num * hall_S),
                        area_To_Split.get_X() + area_To_Split.get_Width(),
                        area_To_Split.get_Y() + (wall_num * hall_S),
                    )
                )
                # add the new wall to the wall list, which the program uses to
                # draw the walls after creating all of them.
                wall_To_Remove = (
                    random.randint(1, area_To_Split.get_Width() / hall_S) - 1
                ) * hall_S
                # print("H Wall to remove: ", wall_To_Remove/hall_S)
                passage_list.append(
                    Wall(
                        area_To_Split.get_X() + wall_To_Remove + 1,
                        area_To_Split.get_Y() + (wall_num * hall_S),
                        area_To_Split.get_X() + wall_To_Remove + hall_S - 1,
                        area_To_Split.get_Y() + (wall_num * hall_S),
                    )
                )

            elif h_V == 1:
                # if a vertical wall
                walls_list.append(
                    Wall(
                        area_To_Split.get_X() + (wall_num * hall_S),
                        area_To_Split.get_Y(),
                        area_To_Split.get_X() + (wall_num * hall_S),
                        area_To_Split.get_Y() + area_To_Split.get_Height(),
                    )
                )
                # add the new wall to the wall list, which the program uses to
                # draw the walls after creating all of them.
                wall_To_Remove = (
                    random.randint(1, area_To_Split.get_Height() / hall_S) - 1
                ) * hall_S
                # print("V Wall to remove: ", wall_To_Remove/hall_S)
                passage_list.append(
                    Wall(
                        area_To_Split.get_X() + (wall_num * hall_S),
                        area_To_Split.get_Y() + wall_To_Remove + 1,
                        area_To_Split.get_X() + (wall_num * hall_S),
                        area_To_Split.get_Y() + wall_To_Remove + hall_S - 1,
                    )
                )

            else:
                pass

            # print("Walls: \n", walls_list)
            # print("Passages: \n", passage_list)
        # end of if done == 0

        else:
            pass

    # End of while done == 0

    print("Escaped")

    message.undraw()
    message = Text(
        Point(maze_S / 2 + offset, maze_S + (offset * 2) - (offset / 2)),
        "Drawing...",
    )
    message.draw(win)

    a = 0
    for f in range(0, len(walls_list)):
        # draws the maze
        W = walls_list[f]
        if a < 3:
            time.sleep(0.5)
            a = a + 0.5
        if hall_S == 10 and maze_S > 150:
            time.sleep(0.005)
        elif hall_S == 25:
            time.sleep(0.05)
        elif maze_S < 700 and hall_S == 50:
            time.sleep(0.08)
        elif maze_S > 650 and hall_S != 50:
            time.sleep(0.3)
        wall = Line(
            Point(W.get_X() + offset, W.get_Y() + offset),
            Point(W.get_X_1() + offset, W.get_Y_1() + offset),
        )
        wall.setFill(color_rgb(0, 0, 0))
        wall.setWidth(2)
        wall.draw(win)

        P = passage_list[f]
        passage = Line(
            Point(P.get_X() + offset, P.get_Y() + offset),
            Point(P.get_X_1() + offset, P.get_Y_1() + offset),
        )
        passage.setFill(color_rgb(240, 240, 240))
        passage.setWidth(2)
        passage.draw(win)

    message.undraw()
    # draws a message indicating to the suer that the maze has finished
    message = Text(
        Point(maze_S / 2 + offset, maze_S + (offset * 2) - (offset / 2)),
        "Finished!",
    )
    message.draw(win)

    if p.lower() == "yes":
        Save_M(win, maze_S, hall_S)

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
    main_Label = tkinter.Label(main, text="Recursive Division").grid(
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
        maze_Size = check_Maze_Size(maze_Size_c)

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
