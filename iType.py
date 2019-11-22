from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def iType2Args(reg1, reg2):
    index = reg2.index("(")
    offset = reg2[0:index]
    offset = int(offset)
    if offset % 4:
        raise Exception("Boundary is not word aligned")
    binaddr = ""
    binaddr += bin(offset).replace("0b", "")
    binaddr = binaddr.zfill(16)
    index2 = reg2.index(")")
    secondReg = reg2[index + 1 : index2]

    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "red")
    writeToFile(regCode1)

    regCode2 = getRegisterCode(secondReg)
    printColor(regCode2, "blue")
    writeToFile(regCode2)

    printColor(binaddr + "\n", "green")
    writeToFile(binaddr + "\n")


def iType3Args(inst, reg1, reg2, dest):
    set1 = ["ADDI", "MULTI", "SUBI", "DIVI"]
    set2 = ["BEQ", "BNE"]
    binaddr = ""

    if inst in set1:
        binaddr += bin(int(dest)).replace("0b", "")
        binaddr = binaddr.zfill(16)

    else:
        for i in range(6, len(dest)):
            binaddr += "{0:04b}".format(int(dest[i], 16))

    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "red")
    writeToFile(regCode1)

    regCode2 = getRegisterCode(reg2)
    printColor(regCode2, "blue")
    writeToFile(regCode2)

    printColor(binaddr + "\n", "green")
    writeToFile(binaddr + "\n")
