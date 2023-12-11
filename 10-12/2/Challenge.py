stepConverterForSymbol = {
  "|": {
    (1, 0): (1, 0),
    (-1, 0): (-1, 0)
  },
  "-": {
    (0, 1): (0, 1),
    (0, -1): (0, -1)
  },
  "L": {
    (0, -1): (-1, 0),
    (1, 0): (0, 1)
  },
  "J": {
    (0, 1): (-1, 0),
    (1, 0): (0, -1)
  },
  "7": {
    (-1, 0): (0, -1),
    (0, 1): (1, 0)
  },
  "F": {
    (-1, 0): (0, 1),
    (0, -1): (1, 0)
  },
}

rows = list(map(list, open('../input.txt').read().splitlines()))

coordHistory = [(112, 18),(112, 19)]
  
def getNextCoordHistory(coordHistory):
  currentCoord = coordHistory[-1]
  lastCoord = coordHistory[-2]

  currentSymbol = rows[currentCoord[0]][currentCoord[1]]
  rows[currentCoord[0]][currentCoord[1]] = "#"
  lastStep = ((currentCoord[0] - lastCoord[0]), (currentCoord[1] - lastCoord[1]))
  try:
    nextStep = stepConverterForSymbol[currentSymbol][lastStep]
  except:
    print("no step found for symbol:", currentSymbol, "using last step:", lastStep, "at coords:", currentCoord, "prev:", las)
  nextCoord = ((currentCoord[0] + nextStep[0]), (currentCoord[1] + nextStep[1]))

  coordHistory.append(nextCoord)
  return coordHistory

def getNextCoords(history):
  history = getNextCoordHistory(history)

while coordHistory[-1] != (113, 18):
  getNextCoords(coordHistory)

rows = list(map(lambda row: "".join(row), rows))

for rowIdx, row in enumerate(rows):
  print(row)
