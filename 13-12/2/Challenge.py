import re

lines = open('../input.txt').read().splitlines()

grids = []
grid = []
for line in lines:
  if(len(line) > 0):
    grid.append(list(line))
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
def getImperfectionIdx(list1, list2):
  scanRange = list(range(min(len(list1), len(list2))))
  for idx in scanRange:
    if(list1[-(idx + 1)] != list2[idx]):
      return len(list1) - idx - 1
  return None

def getReverse(symbol):
  if(symbol == "#"):
    return "."
  elif(symbol == "."):
    return "#"

total = 0
for grid in grids:
  rowImperfections = {}
  colImperfections = {}

  for rowIdx, row in enumerate(grid):
    for colIdx, cell in enumerate(row):
      col = list(map(lambda row: row[colIdx], grid))
      imperfectionIdx = getImperfectionIdx(col[:rowIdx], col[rowIdx:])
      if(type(imperfectionIdx) is int):
        if(rowIdx in rowImperfections):
          rowImperfections[rowIdx].append((imperfectionIdx, colIdx))
        else:
          rowImperfections[rowIdx] = [(imperfectionIdx, colIdx)]
      imperfectionIdx = getImperfectionIdx(row[:colIdx], row[colIdx:])
      if(type(imperfectionIdx) is int):
        if(colIdx in colImperfections):
          colImperfections[colIdx].append((rowIdx, imperfectionIdx))
        else:
          colImperfections[colIdx] = [(rowIdx, imperfectionIdx)]

  fixed = False
  for key in rowImperfections:
    if(len(rowImperfections[key]) == 1):
      tup = rowImperfections[key][0]
      row = tup[0]
      col = tup[1]
      grid[row][col] = getReverse(grid[row][col])
      fixed = True
      total += key*100
  if(not fixed):
    for key in colImperfections:
      if(len(colImperfections[key]) == 1):
        tup = colImperfections[key][0]
        row = tup[0]
        col = tup[1]
        grid[row][col] = getReverse(grid[row][col])
        fixed = True
        total += key
print(total)
