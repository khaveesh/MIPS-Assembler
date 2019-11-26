from getType import getType
from rType import rType
from iType import iType2Args, iType3Args
from jType import jType
from hexAdd import hexAdd
from typing import Dict

with open("input.txt") as file:
    open("out.o", "w").close()
    counter = 0
    icount = 0
    jcount = 0
    rcount = 0
    labelstraddr: Dict[str, str] = {}
    set2 = ["BEQ", "BNE", "BLT", "BGT", "BLTZ", "BLEZ", "BGTZ"]
    while True:
        bad_char = [",", "$", "\\n"]
        string = file.readline()
        if string == "":
            break
        label = string.find(":")
        if label != -1:
            labelstraddr[string[0:label]] = hexAdd(counter)
            string = string[label + 1 :]
        string = "".join([i for i in string if i not in bad_char])
        data = string.split()

        print(hexAdd(counter) + ": ", end="")
        counter += 1

        instType = getType(data[0])
        if instType == "R":
            if len(data) == 2:
                rType(data[0], data[1], "", "")
            elif len(data) == 3:
                rType(data[0], data[1], data[2], "")
            else:
                rType(data[0], data[1], data[2], data[3])
            rcount += 1
        elif instType == "J":
            jType(labelstraddr.get(data[1]))
            jcount += 1
        else:
            if data[0].upper() in set2:
                if len(data) == 3:
                    data[2] = str(labelstraddr.get(data[2]))
                    iType2Args(data[0], data[1], data[2])
                elif len(data) == 4:
                    data[3] = str(labelstraddr.get(data[3]))
                    iType3Args(data[0], data[1], data[2], data[3])
            else:
                if len(data) == 3:
                    iType2Args(data[0], data[1], data[2])
                elif len(data) == 4:
                    iType3Args(data[0], data[1], data[2], data[3])
            icount += 1

    print("Number of R-Type Instructions : " + str(rcount))
    print("Number of I-Type Instructions : " + str(icount))
    print("Number of J-Type Instructions : " + str(jcount))
