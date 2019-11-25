from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def rType(instruction, r1, r2, r3):
    function_decoder = {
        "add": "100000",
        "addu": "100001",
        "and": "100100",
        "div": "011010",
        "divu": "011011",
        "mfhi": "010000",
        "mflo": "010010",
        "mthi": "010001",
        "mtlo": "010011",
        "mult": "011000",
        "multu": "011001",
        "nor": "100111",
        "or": "100101",
        "sll": "000000",
        "sllv": "000100",
        "slt": "101010",
        "sltu": "101011",
        "sra": "000011",
        "srav": "000111",
        "srl": "000010",
        "srlv": "000110",
        "sub": "100010",
        "subu": "100011",
        "xor": "100110",
    }
    shamt = "00000"
    function = function_decoder[instruction]

    if instruction.lower() == "mfhi" or instruction.lower() == "mflo":
        reg1 = "00000"
        reg2 = "00000"
        reg3 = getRegisterCode(r1)

    elif instruction.lower() == "mtlo" or instruction.lower() == "mthi":
        reg1 = getRegisterCode(r1)
        reg2 = "00000"
        reg3 = "00000"

    elif (
        instruction.lower() == "div"
        or instruction.lower() == "divu"
        or instruction.lower() == "mult"
        or instruction.lower() == "multu"
    ):
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r2)
        reg3 = "00000"

    elif (
        instruction.lower() == "sll"
        or instruction.lower() == "sra"
        or instruction.lower() == "srl"
    ):
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r2)
        reg3 = "00000"
        shamt = bin(int(r3))[2:].zfill(5)

    else:
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r2)
        reg3 = getRegisterCode(r3)

    printColor(reg1, "red")
    printColor(reg2, "blue")
    printColor(reg3, "green")
    printColor(shamt, "cyan")
    printColor(function + "\n", "white")
    writeToFile(reg1 + reg2 + reg3 + shamt + function + "\n")
