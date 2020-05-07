from huepy import *


def printColor(string, color):
    flag = ""
    if "\n" in string:
        flag = "\n"
        string = string.rstrip()
    temp = color + "('" + string + "')"
    print(eval(temp), end=flag)
