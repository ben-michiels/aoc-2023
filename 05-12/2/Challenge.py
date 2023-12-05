import re

lines = open('../input.txt').read().splitlines()

seedsAndRanges = list(map(int, re.findall("(\d+)", lines[0])))
lines.pop(0)

seeds = []

class PossibleValues:
  def __init__(self, start, rng):
    self.start = start
    self.rng = rng

for x in range(int(len(seedsAndRanges) / 2)):
  seeds.append(PossibleValues(seedsAndRanges[x * 2], seedsAndRanges[(x * 2) + 1]))

currentSources = seeds.copy()
currentDestinations = []

def toString(value):
  return "{ start: " + str(value.start) + ", rng: " + str(value.rng) + " }"

for line in lines:
  if(len(line) == 0): continue

  if(":" in line):
    currentSources.extend(currentDestinations)
    currentDestinations = []
    continue
  
  newSources = currentSources.copy()
  numbers = list(map(int, re.findall("(\d+)", line)))
  destinationStart = numbers[0]
  sourceStart = numbers[1]
  rangeLength = numbers[2]

  for sourceIdx, source in enumerate(currentSources):
    if(sourceStart < (source.start + source.rng) and source.start < (sourceStart + rangeLength)):
      # consume source
      newSources.remove(source)

      # add back the start of the source if unmapped
      if(source.start < sourceStart):
        start = source.start
        rng = sourceStart - source.start
        newSources.append(PossibleValues(start, rng))

      # add back the end of the source if unmapped
      if((sourceStart + rangeLength) < (source.start + source.rng)):
        start = sourceStart + rangeLength
        rng = (source.start + source.rng) - start
        newSources.append(PossibleValues(start, rng))

      minStart = source.start if source.start > sourceStart else sourceStart
      usedRangeLength = (minStart - sourceStart)
      start = destinationStart + usedRangeLength
      rng = min(rangeLength - usedRangeLength, (source.start + source.rng) - minStart)
      currentDestinations.append(PossibleValues(start, rng))
  
  currentSources = newSources

currentDestinations.extend(currentSources)
def getStart(possibleValues):
  return possibleValues.start

print(min(list(map(getStart, currentDestinations))))