# Author: Jacob Stringer

def cV(sNi, flNi, value):
    type = "none"
    if isinstance(value, str):
        if sNi == True:
            if ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in value:
                type = "iStr"
            else:
                type = "str"
        if sNi == False:
            type = "str"



    if isinstance(value, int):
        if flNi == True:
            type = "float"
        elif flNi == False:
            type = "int"

    if isinstance(value, float):
        type = "float"
    return type
