# Author: Jacob Stringer

# CheckValue is used by calling CheckValue.cV(sNi, flNi, value) and returns a
# string of the type of the value.

# sNi (string Not int) is a true false value that tells it whether or not this
# value needs to be checked as a string that will never have a number in it.

# flNi (float Not int) is a true false value that tells checkvalue whether to
# return float or int when the value's isinstance equals int. Because somtimes
# a float can be entered and evaluated as an int.


def cV(sNi, flNi, value):
    type = "none"
    if isinstance(value, str):
        if sNi is True:
            if (
                "0"
                or "1"
                or "2"
                or "3"
                or "4"
                or "5"
                or "6"
                or "7"
                or "8"
                or "9"
            ) in value:
                type = "iStr"
            else:
                type = "str"
        if sNi is False:
            type = "str"

    if isinstance(value, int):
        if flNi is True:
            type = "float"
        elif flNi is False:
            type = "int"

    if isinstance(value, float):
        type = "float"
    return type
