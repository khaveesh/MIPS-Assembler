from getType import getType
from rType import rType
import csv
with open("input.txt") as file:
    while True:
        bad_char = [',', '$']
        string = file.readline()
        if string == "":
            break
        comma = ','
        #string.replace(comma, '')
        string = filter(lambda i: i not in bad_char, string)
        print string
        data = string.split()
        print data
        # reader = csv.reader(file, delimiter = '\n')
        # for row in reader:
        #     print row
        #     data = row.split()
        #     print data
        instType = getType(data[0])
        print instType