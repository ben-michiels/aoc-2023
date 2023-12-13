import re

lines = open('../input.txt').read().splitlines()

grids = []
grid = []
for line in lines:
  if(len(line) > 0):
    grid.append(line)
  else:
    grids.append(grid)
    grid = []
if(len(grid) > 0):
  grids.append(grid)

def isReflection(list1, list2):
  scanRange = list(range(min(len(list1), len(list2))))
  for idx in scanRange:
    if(list1[-(idx + 1)] != list2[idx]):
      return False
  return True

total = 0
for grid in grids:
  possibleRows = list(range(1, len(grid)))
  possibleCols = list(range(1, len(grid[0])))

  for rowIdx, row in enumerate(grid):
    if(not isReflection(grid[:rowIdx], grid[rowIdx:])):  
      if(possibleRows.count(rowIdx)):
        possibleRows.pop(possibleRows.index(rowIdx))

    for colIdx, cell in enumerate(row):
      if(not isReflection(row[:colIdx], row[colIdx:])):
        if(possibleCols.count(colIdx)):
          possibleCols.pop(possibleCols.index(colIdx))

  for rowIdx in possibleRows:
    total += 100*rowIdx
  for colIdx in possibleCols:
    total += colIdx

print(total)
