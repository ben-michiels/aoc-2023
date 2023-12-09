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
  for differences in allDifferences:
    prediction += differences[-1]

  predictionSum += prediction

print(predictionSum)