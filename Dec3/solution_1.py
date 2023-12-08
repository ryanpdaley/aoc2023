import re
f = open('data.txt', 'r')
dataRows = f.readlines()

# dataRows = ['467..114..',
#             '...*......',
#             '..35..633.',
#             '......#...',
#             '617*......',
#             '.....+.58.',
#             '..592.....',
#             '......755.',
#             '...$.*....',
#             '.664.598..']

# dataRows = ['............409..........784...578...802......64..............................486.248..............177....................369...............',
#             '.....-939..........524#...#....=.......*.........+......90.................................76..615..-..@.....961..........$.......*.........',
#             '............951*........................736...955..258....*.....253@.............210.10.....=...*.......776...*....&...............600..274.',
#             '152.78..........671.....936.......................*..........14...............................575.=.........214..519.....787.739........*...',
#             '...*....591......................514*155..........807...............516.............23...5#.......250.531...................*......-..71....',
#             '.............................................254..........69&........*..............*....................*...............*........785.......',
#             '....5....../.42..908*166..242*825.....................19%............148..822......127..+...+...........971...........206.540.753...........'
#             ]

expectedSymbols = ['!', '@', '#', '$', '%', '^',
                   '&', '*', '(', ')', '_', '+', '=', '-', '/']

regex = r"\d+"


def checkAround(match, row, index):
    checkStr = ''
    l = max(match.start()-1, 0)
    r = min(match.end()+1, len(row)-1)
    t = max(index-1, 0)
    b = min(index+1, len(dataRows)-1)
    for checkRow in range(t, b+1):
        for checkCol in range(l, r):
            checkStr += str(dataRows[checkRow][checkCol])
    for symbol in expectedSymbols:
        if symbol in checkStr:
            return True
    return False


count = 0
for rowIndex in range(0, len(dataRows)):
    cleanRow = dataRows[rowIndex].strip()
    matches = re.finditer(regex, cleanRow)
    for match in matches:
        isValid = checkAround(match, cleanRow, rowIndex)
        if (isValid):
            count += int(match.group())
print('-----')
print("Total: " + str(count))
print('-----')
