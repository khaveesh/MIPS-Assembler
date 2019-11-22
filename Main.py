from getType import getType
from rType import rType
import csv
with open("input.txt") as file:
    while True:
        bad_char = [',', '$']
        string = file.readline()
        if string == "":
            break
        comma = ','
        #string.replace(comma, '')
        #string.replace('$', '')
        #string = str(filter(lambda i: i not in bad_char, string))
        print (string)
        message = "".join([i for i in string if i not in bad_char])
        print(message)
        data = string.split(" ", 0)
        print (data)
        instType = getType(data[0])
        print (instType)
