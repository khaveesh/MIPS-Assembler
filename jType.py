from termcolor import colored
from writeToFile import writeToFile
from printColor import printColor


def jType(address):
    binaddr = ""
    for i in range(3, len(address)):
        binaddr += "{0:04b}".format(int(address[i], 16))
    printColor(binaddr[2:-1], "red")
    writeToFile(binaddr[2:-1] + "\n")
