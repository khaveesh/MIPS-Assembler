from writeToFile import writeToFile
from printColor import printColor


def jType(address):
    binaddr = ""
    for i in range(3, len(address)):
        binaddr += "{0:04b}".format(int(address[i], 16))
    binaddr = "00" + binaddr[2:-2]
    printColor(binaddr + "\n", "red")
    writeToFile(binaddr + "\n")
