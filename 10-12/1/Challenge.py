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

rows = open('../input.txt').read().splitlines()

coordHistoryA = [(112, 18),(112, 19)]
coordHistoryB = [(112, 18),(113, 18)]

  
def getNextCoordHistory(coordHistory):
  currentCoord = coordHistory[-1]
  lastCoord = coordHistory[-2]

  currentSymbol = rows[currentCoord[0]][currentCoord[1]]
  lastStep = ((currentCoord[0] - lastCoord[0]), (currentCoord[1] - lastCoord[1]))
  try:
    nextStep = stepConverterForSymbol[currentSymbol][lastStep]
  except:
    print("no step found for symbol:", currentSymbol, "using last step:", lastStep, "at coords:", currentCoord, "prev:", las)
  nextCoord = ((currentCoord[0] + nextStep[0]), (currentCoord[1] + nextStep[1]))

  coordHistory.append(nextCoord)
  return coordHistory

def getNextCoords(coordHistory1, coordHistory2):
  coordHistory1 = getNextCoordHistory(coordHistory1)
  coordHistory2 = getNextCoordHistory(coordHistory2)

while(coordHistoryA[-1] != coordHistoryB[-1] and coordHistoryA[-1] != coordHistoryB[-2]):
  getNextCoords(coordHistoryA, coordHistoryB)

print(len(coordHistoryA))