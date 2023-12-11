rows = list(map(list, open('../input.txt').read().splitlines()))

rowsToExpand = list(range(140))
colsToExpand = list(range(140))

for rowIdx, row in enumerate(rows):
  for colIdx, cell in enumerate(row):
    if(cell == "#"):
      if(rowsToExpand.count(rowIdx)):
        rowsToExpand.pop(rowsToExpand.index(rowIdx))
      if(colsToExpand.count(colIdx)):
        colsToExpand.pop(colsToExpand.index(colIdx))

distanceSum = 0
galaxyCoords = []
for rowIdx, row in enumerate(rows):
  for colIdx, cell in enumerate(row):
    if(cell == "#"):
      currentCoord = (rowIdx, colIdx)
      for coord in galaxyCoords:
        rowDiff = abs(currentCoord[0] - coord[0])
        rowRange = range(coord[0], currentCoord[0]) if currentCoord[0] > coord[0] else range(currentCoord[0], coord[0])
        for index in rowRange:
          if(index in rowsToExpand):
            rowDiff += 999999

        colDiff = abs(currentCoord[1] - coord[1])
        colRange = range(coord[1], currentCoord[1]) if currentCoord[1] > coord[1] else range(currentCoord[1], coord[1])
        for index in colRange:
          if(index in colsToExpand):
            colDiff += 999999


        distanceSum += (rowDiff + colDiff)
      galaxyCoords.append(currentCoord)

print(distanceSum)