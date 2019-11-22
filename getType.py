# This function looks at the opCode and returns the type of the function.

# 32
from printColor import printColor

def getType(inst):
    # Having three sets, if return the instruction based on which set it is present at.
    #print "Received instruction = " + inst
    if inst.upper() in rType:
        # Have print statement printing 0s
        printColor("00000000", "yellow")
        return 'R'

    rType = ["ADD", "SUB", "MULT"]
    iType = ["ADDI", "LW", "SW", "SUBI"]
    opcode = 
    {
        'ADDI' : "001000",
        'LW' : "100011",
        'SW' : "101011",
        'BEQ' : "000100"
        'J' : "000010",
        'SLT' : "101010",
        'BGTZ' : "000111",
        "BNE" : "000101",
        "BLEZ" : "000110",
        "SLTI" : "001010"
    }
    elif inst.upper() in iType:

        printColor(opcode[inst.upper()], "yellow")
        return 'I'
    else:
        return 'J'