# Author: Jacob Stringer

def cV( value, sNi = False, flNi = False):
    type = "none"

    if isinstance(value, str):
        if sNi:
            if ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in value:
                type = "iStr"
            else:
                type = "str"
        else:
            type = "str"

    if isinstance(value, int):
        if flNi:
            type = "float"
        else:
            type = "int"

    if isinstance(value, float):
        type = "float"

    return type
