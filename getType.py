# This function looks at the opCode and returns the type of the function.

# 32
def getType(inst):
    # Having three sets, if return the instruction based on which set it is present at.
    #print "Received instruction = " + inst
    rType = ["ADD", "SUB", "MUL"]
    iType = ["ADDI", "lw", "sw"]
    if inst in rType:
        return 'R'
    elif inst in iType:
        return 'I'
    else:
        return 'J'