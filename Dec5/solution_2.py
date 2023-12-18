import functools
f = open('data.txt', 'r')
dataRows = f.readlines()

groups = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
          'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']


def getSeedRanges():
    seeds = []
    seedStr = dataRows[0].strip().split('seeds: ')[1].split(' ')
    rawSeeds = [int(x) for x in seedStr]
    rawSeedLength = len(rawSeeds)
    for x in range(0, rawSeedLength, 2):
        seedRange = [rawSeeds[x], rawSeeds[x] + rawSeeds[x+1]]
        seeds.append(seedRange)
    return seeds


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


@functools.lru_cache
def cachedSeed(seed):
    id = seed
    for group in groups:
        map = getMap(group)
        id = findMapping(id, map)
    return id


def solution():
    minLocation = 100000000000000
    seedRanges = getSeedRanges()
    for seedRange in seedRanges:
        for seed in range(seedRange[0], seedRange[1]):
            print(seed)
            id = cachedSeed(seed)
            minLocation = min(minLocation, id)
    print(minLocation)


solution()
