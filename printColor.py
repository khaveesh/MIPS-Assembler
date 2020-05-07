import huepy


def printColor(string, color):
    flag = ""
    if "\n" in string:
        flag = "\n"
        string = string.rstrip()
    temp = "huepy.{0}('{1}')".format(color, string)
    print(eval(temp), end=flag)
