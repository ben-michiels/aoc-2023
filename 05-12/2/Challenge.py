import re

lines = open('../input.txt').read().splitlines()

seedsAndRanges = list(map(int, re.findall("(\d+)", lines[0])))
lines.pop(0)

seeds = []

class PossibleValues:
  def __init__(self, start, rng):
    self.start = start
    self.rng = rng

for x in range(10):
  seeds.append(PossibleValues(seedsAndRanges[x * 2], seedsAndRanges[(x * 2) + 1]))

currentSources = seeds.copy()
currentDestinations = seeds.copy()


for line in lines:
  if(len(line) == 0): continue

  if(":" in line):
    currentSources = currentDestinations.copy()
    continue
  
  numbers = list(map(int, re.findall("(\d+)", line)))
  destinationStart = numbers[0]
  sourceStart = numbers[1]
  rangeLength = numbers[2]

  for sourceIdx, source in enumerate(currentSources):
    if(sourceStart < (source.start + source.rng) and source.start < (sourceStart + rangeLength)):
      minStart = source.start if source.start > sourceStart else sourceStart
      usedRangeLength = (minStart - sourceStart)
      start = destinationStart + usedRangeLength
      rng = min(rangeLength - usedRangeLength, (source.start + source.rng) - minStart)
      currentDestinations[sourceIdx] = PossibleValues(start, rng)

def getStart(possibleValues):
  return possibleValues.start

print(min(list(map(getStart, currentDestinations))))