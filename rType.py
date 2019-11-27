from printColor import printColor
from getRegisterCode import getRegisterCode
from writeToFile import writeToFile

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
    "move": "100001",
    "negu": "100011",
    "not": "100111",
    "movn": "001011",
    "movz": "001010",
}


def rType(instruction, r1, r2, r3):
    # r1 = rd
    # r2 = rs
    # r3 = rt
    shamt = "00000"
    instruction = instruction.lower()
    function = function_decoder[instruction]
    if instruction == "mfhi" or instruction == "mflo":
        reg1 = getRegisterCode(r1)
        reg2 = "00000"
        reg3 = "00000"
    elif instruction == "mtlo" or instruction == "mthi":
        reg1 = "00000"
        reg2 = getRegisterCode(r1)
        reg3 = "00000"
    elif (
        instruction == "div"
        or instruction == "divu"
        or instruction == "mult"
        or instruction == "multu"
    ):
        reg1 = "00000"
        reg2 = getRegisterCode(r1)
        reg3 = getRegisterCode(r2)
    elif instruction == "sll" or instruction == "sra" or instruction == "srl":
        reg1 = getRegisterCode(r1)
        reg2 = "00000"
        reg3 = getRegisterCode(r2)
        shamt = "{0:05b}".format(int(r3))
    elif instruction == "move" or instruction == "negu":
        reg1 = getRegisterCode(r1)
        reg2 = "00000"
        reg3 = getRegisterCode(r2)
    elif instruction == "not":
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r2)
        reg3 = "00000"
    elif instruction == "sllv" or instruction == "srav" or instruction == "srlv":
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r3)
        reg3 = getRegisterCode(r2)
    else:
        reg1 = getRegisterCode(r1)
        reg2 = getRegisterCode(r2)
        reg3 = getRegisterCode(r3)
    printColor(reg2, "blue")
    printColor(reg3, "green")
    printColor(reg1, "red")
    printColor(shamt, "cyan")
    printColor(function + "\n", "grey")
    writeToFile(reg2)
    writeToFile(reg3)
    writeToFile(reg1)
    writeToFile(shamt)
    writeToFile(function + "\n")
