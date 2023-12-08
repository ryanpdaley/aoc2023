import re
f = open('data.txt', 'r')
dataRows = f.readlines()

regex_star = r"\*"
regex_numbers = r"\d+"


def getNumbers(coords):
    numbers = []
    for i in range(0, len(coords)):
        x = int(coords[i][0])
        y = int(coords[i][1])
        cleanRow = dataRows[x].strip()
        matches_star = re.finditer(regex_numbers, cleanRow)
        for match in matches_star:
            start = int(match.start())
            end = int(match.end())
            if y >= start and y <= end:
                numbers.append(match.group())
    ratios = list(set(numbers))
    return int(ratios[0]) * int(ratios[-1])


def checkAroundStar(x, y):
    checkStr = ''
    numsCoords = []
    l = max(x-1, 0)
    r = min(x+1, colCount-1)
    t = max(y-1, 0)
    b = min(y+1, rowCount-1)
    for checkRow in range(t, b+1):
        for checkCol in range(l, r+1):
            item = dataRows[checkRow][checkCol]
            checkStr += str(item)
            if (item.isdigit()):
                numsCoords.append([checkRow, checkCol])
        checkStr += '|'
    matches_numbers = re.findall(regex_numbers, checkStr)
    if (len(matches_numbers) > 1):
        return getNumbers(numsCoords)
    return 0


count = 0
matchCoords = []
rowCount = len(dataRows)
colCount = len(dataRows[0])
for rowIndex in range(0, len(dataRows)):
    cleanRow = dataRows[rowIndex].strip()
    matches_star = re.finditer(regex_star, cleanRow)
    for match in matches_star:
        starSearch = checkAroundStar(match.start(), rowIndex)
        count += starSearch
print('-----')
print("Total: " + str(count))
print('-----')
