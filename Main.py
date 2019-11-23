from getType import *
from rType import *
from iType import *
from jType import *
from hexAdd import *

with open("input.txt") as file:
    open("out.o", "w").close()
    counter = 0
    icount = 0
    jcount = 0
    rcount = 0
    while True:
        bad_char = [",", "$", "\\n"]
        string = file.readline()
        if string == "":
            break
        string = "".join([i for i in string if i not in bad_char])
        data = string.split()

        print(hexAdd(counter) + ": ", end="")
        counter += 1

        instType = getType(data[0])
        if instType == "R":
            rType(data[0], data[1], data[2], data[3])
            rcount += 1
        elif instType == "J":
            jType(data[1])
            jcount += 1
        else:
            if len(data) == 3:
                iType2Args(data[0], data[1], data[2])
            elif len(data) == 4:
                iType3Args(data[0], data[1], data[2], data[3])
            icount += 1

    print("Number of R-Type Instructions : " + str(rcount))
    print("Number of I-Type Instructions : " + str(icount))
    print("Number of J-Type Instructions : " + str(jcount))
