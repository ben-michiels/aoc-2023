times = [45, 98, 83, 73]
distances = [295, 1734, 1278, 1210]

waysToWinPerGame = []

for idx, time in enumerate(times):
  waysToWin = 0
  distance = distances[idx]
  for chargeTime in range(time):
    if(chargeTime * (time - chargeTime) > distance):
      waysToWin += 1
  waysToWinPerGame.append(waysToWin)

print(waysToWinPerGame[0] * waysToWinPerGame[1] * waysToWinPerGame[2] * waysToWinPerGame[3])