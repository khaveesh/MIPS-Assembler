from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def iType2Args(inst, reg1, reg2):
    if inst.upper() == "LI":
        regCode2 = getRegisterCode(reg1)
        printColor(regCode2, "red")
        writeToFile(regCode2)

        binaddr = ""
        if int(reg2) >= 0:
            binaddr += bin(int(reg2)).replace("0b", "")
            binaddr = binaddr.zfill(21)
        else:
            num = 65535 + int(reg2)
            num = num + 1
            num = str(num)
            binaddr += bin(int(num)).replace("0b", "")
            binaddr = binaddr.zfill(16)
        printColor(binaddr + "\n", "green")
        writeToFile(binaddr + "\n")
    else:
        l = ["SW", "LW"]
        if inst.upper() not in l:
            raise Exception(" Wrong instruction format")

        index = reg2.index("(")
        offset = reg2[0:index]
        offset = int(offset)
        if offset % 4:
            raise Exception(" Boundary is not word aligned")
        binaddr = ""
        binaddr += bin(offset).replace("0b", "")
        binaddr = binaddr.zfill(16)
        index2 = reg2.index(")")
        secondReg = reg2[(index + 1) : index2]

        regCode2 = getRegisterCode(secondReg)
        printColor(regCode2, "red")
        writeToFile(regCode2)
        regCode1 = getRegisterCode(reg1)
        printColor(regCode1, "blue")
        writeToFile(regCode1)
        printColor(binaddr + "\n", "green")
        writeToFile(binaddr + "\n")


def iType3Args(inst, reg1, reg2, dest):
    set1 = ["ADDI", "SUBI", "DIVI", "SLTI", "ORI", "ANDI", "XORI"]
    set2 = ["BEQ", "BNE", "BLT", "BGT"]
    binaddr = ""

    if inst.upper() in set1:
        if int(dest) >= 0:
            #binaddr += bin(int(dest, 16)).replace("0b", "")
            binaddr += bin(int(dest)).replace("0b", "")
            binaddr = binaddr.zfill(16)
        else:
            num = 65535 + int(dest)
            num = num + 1
            #print(num)
            num = str(num)
            #print(num)
            binaddr += bin(int(num)).replace("0b", "")
            binaddr = binaddr.zfill(16)

    elif inst.upper() in set2:
        for i in range(6, len(dest)):
            binaddr += "{0:04b}".format(int(dest[i], 16))
        binaddr = binaddr[0:-2]
        binaddr = "00" + binaddr

    regCode2 = getRegisterCode(reg2)
    printColor(regCode2, "red")
    writeToFile(regCode2)

    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "blue")
    writeToFile(regCode1)

    printColor(binaddr + "\n", "green")
    writeToFile(binaddr + "\n")
