from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def iType2Args(reg1, reg2):

    index = reg2.find("(")
    offset = reg2[0:index]
    offset = int(offset)
    tbinaddr = ""
    binaddr = ""
    tbinaddr += bin(offset).replace("0b", "")
    for i in range(0, 16 - len(tbinaddr)):
        binaddr += "0"
    binaddr += tbinaddr
    index2 = reg2.find(")")

    secondReg = reg2[index + 1, index2]

    regCode1 = getRegisterCode(reg1)

    printColor(regCode1, "red")
    writeToFile(re)

    regCode2 = getRegisterCode(secondReg)
    printColor(regCode2, "red")
    writeToFile(regCode2)

    printColor(offset)
    writeToFile
    # Print 16 bit Immediate value


def iType3Args(reg1, reg2, value):
    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "")
    writeToFile(regCode1)
    regCode2 = getRegisterCode(reg2)
    printColor(regCode2, "")
    writeToFile(regCode2)
    regCode3 = getRegisterCode(reg3)
    printColor(regCode3, "")
    writeToFile(regCode3)
