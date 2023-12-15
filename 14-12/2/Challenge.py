import re

cols = list(map(list, open('../input.txt').read().splitlines()))

total = 0

states = []

def cycleCols(cols):
  for i in range(4):
    rotatedCols = [[]]*100
    for col in cols:
      for idx, char in enumerate(col):
        rotatedCols[idx].append(char)
    cols = rotatedCols

    sortedCols = []
    for col in cols:
      sortedCol = []
      startIdx = 0
      for charIdx, char in enumerate(col):
        if(char == "#"):
          sortedCol.extend(sorted(col[startIdx:charIdx + 1], reverse=True))
          startIdx = charIdx + 1
      sortedCol.extend(sorted(col[startIdx:], reverse=True))
      sortedCols.append(sortedCols)
    cols = sortedCols
  states.append(cols)

for i in range(1000000000):
  if(any(states.count(state) != 1 for state in states)):
    break
  cycleCols(cols)

for i in range(1000000000 % len(states)):
  cycleCols(cols)

def countWeight(cols):
  for col in cols:
    for charIdx, char in enumerate(col):
      if(char == "O"):
        total += (100 - charIdx)  

print(countWeight(cols))
