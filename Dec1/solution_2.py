import re

f = open('data.txt', 'r')
dataRows = f.readlines()

intStrs = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']


def checkString(string):
    found = []
    for n in range(len(string)):
        if (string[n].isdigit()):
            found.append(string[n])
        else:
            for i in intStrs:
                maxRemaining = min(len(string), len(i)+n)
                window = string[n:maxRemaining]
                if (window == i):
                    found.append(intStrs.index(i))
                    break
    firstNumber = int(found[0])*10
    lastNumber = int(found[-1])
    lineTotal = firstNumber + lastNumber
    print("{0} -> {1}".format(string, lineTotal))
    return lineTotal


count = 0
for row in dataRows:
    cleanRow = row.strip()
    count += checkString(cleanRow)
print('-----')
print("Total: " + str(count))
print('-----')
