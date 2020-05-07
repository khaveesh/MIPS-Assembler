def getRegisterCode(reg):
    registers = {
        "0": "00000",
        "t0": "01000",
        "t1": "01001",
        "t2": "01010",
        "t3": "01011",
        "t4": "01100",
        "t5": "01101",
        "t6": "01110",
        "t7": "01111",
        "s0": "10000",
        "s1": "10001",
        "s2": "10010",
        "s3": "10011",
        "s4": "10100",
        "s5": "10101",
        "s6": "10110",
        "s7": "10111",
        "t8": "11000",
        "t9": "11001",
    }
    try:
        return registers[reg]
    except KeyError:
        raise Exception("Invalid register inputted: {0}".format(reg))
