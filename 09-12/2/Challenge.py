import re

lines = open('../input.txt').read().splitlines()

def getDifferences(sequence):
  differences = []
  for n in range(len(sequence) - 1):
    differences.append(sequence[n + 1] - sequence[n])
  return differences

predictionSum = 0

for line in lines:
  sequence = list(map(int, re.findall("(\S+)", line)))
  allDifferences = [sequence]

  while any(difference != 0 for difference in allDifferences[-1]):
    allDifferences.append(getDifferences(allDifferences[-1]))
  
  allDifferences.pop()
  prediction = 0
  for i, differences in enumerate(allDifferences):
    if i % 2:
      prediction -= differences[0]
    else:
      prediction += differences[0]

  predictionSum += prediction

print(predictionSum)