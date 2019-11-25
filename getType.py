# This function looks at the opCode and returns the type of the function.

from printColor import printColor
from writeToFile import writeToFile


def getType(inst):
    rType = [
        "AND",
        "SUBU",
        "MFLO",
        "MFHI",
        "SLTU",
        "ADDU",
        "XOR",
        "SUB",
        "ADD",
        "NOR",
        "SRLV",
        "SRAV",
        "DIVU",
        "MULT",
        "SRA",
        "SLT",
        "SLLV",
        "SRL",
        "SLL",
        "MTLO",
        "MTHI",
        "DIV",
        "OR",
        "MULTU",
    ]
    iType = ["ADDI", "LW", "SW", "SUBI", "SLTI", "BLEZ"]
    opcode = {
        # R - TYPE
        # ALL THE R TYPE HAVE 00000000 OPCODE.
        # I - TYPE
        "ADDI": "001000",
        "SLTI": "001010",
        "LW": "100011",
        "SW": "101011",
        "BEQ": "000100",
        "BGTZ": "000111",
        "BNE": "000101",
        "BLEZ": "000110",
        # J - TYPE
        "J": "000010",
    }

    if inst.upper() in rType:
        printColor("00000000", "yellow")
        writeToFile("00000000")
        return "R"

    elif inst.upper() in iType:
        printColor(opcode[inst.upper()], "yellow")
        writeToFile(opcode[inst.upper()])
        return "I"

    elif inst.upper() == "J":
        printColor(opcode["J"], "yellow")
        writeToFile(opcode["J"])
        return "J"

    else:
        # raise Exception("Invalid OpCode : " + inst)
        print("Invalid opCode")
