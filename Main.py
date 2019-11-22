from getType import getType
from rType import rType
from iType import *
import csv
with open("input.txt") as file:
    while True:
        bad_char = [',', '$', '\\n']
        string = file.readline()
        if string == "":
            break
        string = "".join([i for i in string if i not in bad_char])
        data = string.split()
        print (data)
        instType = getType(data[0])
        if(instType == 'R'):
            rType()
        elif(instType == 'J'):
            jType(data[1])
        else:
            if(len(data) == 3):
                iType2Args(data[1], data[2])
            elif(len(data) == 4):
                iType3Args(data[1], data[2], data[3])
        print (instType)
