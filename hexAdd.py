def hexAdd(i):
    s = "0x00400000"
    s = int(s, 16)
    s += i * 4
    s = str(hex(s))
    return "0x" + s[2:].zfill(8)
