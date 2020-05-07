from printColor import printColor
from writeToFile import writeToFile


def jType(address):
    binaddr = ""
    for i in range(3, len(address)):
        binaddr += "{0:04b}".format(int(address[i], 16))
    binaddr = "00" + binaddr[2:-2]
    printColor(binaddr + "\n", "red")
    writeToFile(binaddr + "\n")
