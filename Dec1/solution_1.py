import re

f = open('data.txt', 'r')
dataRows = f.readlines()

count = 0
for row in dataRows:
    cleanRow = row.strip()
    numbers = re.findall('[0-9]', cleanRow)
    firstNumber = int(numbers[0])*10
    lastNumber = int(numbers[-1])
    lineTotal = firstNumber + lastNumber
    print("{0} -> {1}".format(cleanRow, lineTotal))
    count += lineTotal
print('-----')
print("Total: " + str(count))
print('-----')
