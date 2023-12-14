# f = open('data.txt', 'r')
f = open('sampleData.txt', 'r')
dataRows = f.readlines()

groups = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
          'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']


def getSeeds():
    return dataRows[0].strip().split('seeds: ')[1].split(' ')


def getMap(header):
    mapInfo = []
    saveToMapInfo = False
    for row in dataRows:
        cleanRow = row.strip()
        if saveToMapInfo:
            if cleanRow.endswith(':'):
                return mapInfo
            elif not cleanRow == '':
                mapInfo.append(row.rstrip().split(' '))
        if cleanRow == header:
            saveToMapInfo = True
    return mapInfo


def findMapping(id, map):
    for mapInfo in map:
        intId = int(id)
        int0 = int(mapInfo[0])
        int1 = int(mapInfo[1])
        int2 = int(mapInfo[2])
        if (intId >= int1 and intId < (int1 + int2)):
            found = intId - int1 + int0
            return found
    return id


def solution():
    locations = []
    seeds = getSeeds()
    for seed in seeds:
        print("--------------------------------")
        id = seed
        for group in groups:
            map = getMap(group)
            print("{0} Looking for {1} in {2}".format(group, id, map))
            id = findMapping(id, map)
        locations.append(id)
    print(min(locations))


solution()
