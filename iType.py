from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def iType2Args(reg1, reg2):

    index = reg2.index("(")
    print(index)
    offset = reg2[0:index]
    offset = int(offset)
    print(offset + 2)
    tbinaddr = ""
    binaddr = ""
    tbinaddr += bin(offset).replace("0b", "")
    for i in range(0, 16 - len(tbinaddr)):
        binaddr += "0"
    binaddr += tbinaddr
    index2 = reg2.index(")")
    print(index2)
    secondReg = reg2[index + 1 : index2]

    regCode1 = getRegisterCode(reg1)

    printColor(regCode1, "red")
    writeToFile(regCode1)

    regCode2 = getRegisterCode(secondReg)
    printColor(regCode2, "blue")
    writeToFile(regCode2)

    printColor(binaddr + "\n", "green")
    writeToFile(binaddr + "\n")
    # Print 16 bit Immediate value


def iType3Args(inst, reg1, reg2, dest):
    set1 = ["ADDI", "MULTI", "SUBI", "DIVI"]
    set2 = ["BEQ", "BNE"]
    binaddr = ""
    if inst in set1:
        tbinaddr = ""
        tbinaddr += bin(dest).replace("0b", "")
        for i in range(0, 16 - len(tbinaddr)):
            binaddr += "0"
        binaddr += tbinaddr

    else:
        for i in range(6, len(dest)):
            binaddr += "{0:04b}".format(int(dest), 16)
    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "red")
    writeToFile(regCode1)

    regCode2 = getRegisterCode(reg2)
    printColor(regCode2, "blue")
    writeToFile(regCode2)
    printColor(binaddr, "green")
    writeToFile(binaddr + "\n")


iType2Args("s0", "5(s1)")
