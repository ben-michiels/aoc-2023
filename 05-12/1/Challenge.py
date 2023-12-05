import re

lines = open('../input.txt').read().splitlines()

seeds = list(map(int, re.findall("(\d+)", lines[0])))
lines.pop(0)

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
    if(sourceStart < source and source < (sourceStart + rangeLength)):
      currentDestinations[sourceIdx] = destinationStart + (source - sourceStart)

print(min(currentDestinations))