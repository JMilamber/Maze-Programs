#       Author- Jacob Stringer
#       Date started - 11/12/2019


def strToInt(value_str):
    value_int = 0
    valueInt_asStr = ""
    value_ToAdd = ""
    value_toCheck = ""
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, len(value_str)):
        value_toCheck = value_str[i]
        if value_toCheck in num_list:
            valueInt_asStr = valueInt_asStr + value_toCheck
        if value_toCheck not in num_list:
            pass
    value_str = valueInt_asStr
    for i in range(0, len(value_str)):
        #iterates through the entire string
        value_ToAdd = value_str[i]
        #value to hold the current char being investigated
        if value_ToAdd == "0":
            #since we are using 10** to get the right places for number, adding
            #a zero wont do anything since 0*10**anything = 0
            pass
        elif value_ToAdd == "1":
            value_int = value_int + (1 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "2":
            value_int = value_int + (2 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "3":
            value_int = value_int + (3 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "4":
            value_int = value_int + (4 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "5":
            value_int = value_int + (5 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "6":
            value_int = value_int + (6 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "7":
            value_int = value_int + (7 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "8":
            value_int = value_int + (8 * (10 ** (len(value_str)-(i + 1))))
        elif value_ToAdd == "9":
            value_int = value_int + (9 * (10 ** (len(value_str)-(i + 1))))
        else:
            pass
    return value_int
#end strToInt

def main():
    print("\n----stringToNumber.py help----")
    print("\n     stringToNumber contains a single method called strToInt")
    print("\n     That method takes a single parameter, a string that consists solely of numbers")
    print("\n     I.e : x = stringToNumber.strToInt('5067')")
    print("\n     stringToNumber then converts said string into a int and returns the integer")
    print("\n ----closing help----")
if __name__ == '__main__':
    main()
