time = 45988373
distance = 295173412781210

waysToWin = 0
for chargeTime in range(time):
  if(chargeTime * (time - chargeTime) > distance):
    waysToWin += 1


print(waysToWin)