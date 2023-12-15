import re

lines = open('../input.txt').read().splitlines()

cols = [""]*100
for line in lines:
  for idx, char in enumerate(line):
    cols[idx] += char

total = 0

for col in cols:
  sortedCol = []
  startIndx = 0

  for charIdx, char in enumerate(col):
    if(char == "#"):
      sortedCol.extend(sorted(col[startIndx:charIdx + 1], reverse=True))
      startIndx = charIdx + 1
      
  sortedCol.extend(sorted(col[startIndx:], reverse=True))
  for charIdx, char in enumerate(sortedCol):
    if(char == "O"):
      total += (100 - charIdx)


print(total)
