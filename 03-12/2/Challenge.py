lines = open('../input.txt').read().splitlines()

count = 0


def findNumber(line, charIdx):
  numberString = line[charIdx]

  currentIdx = charIdx - 1
  
  while currentIdx >= 0 and line[currentIdx].isnumeric():
    numberString = line[currentIdx] + numberString
    currentIdx -= 1
  currentIdx = charIdx + 1
  while currentIdx <= 139 and line[currentIdx].isnumeric():
    numberString += line[currentIdx]
    currentIdx += 1

  return numberString
  

for lineIdx, line in enumerate(lines):
  for charIdx, char in enumerate(line):
    if(char == "*"):
      numbers = list([])

      r = range(charIdx - 1 if charIdx > 0 else 0, charIdx + 2 if charIdx != 139 else 140)

      if((lineIdx - 1) >= 0):
        newNumber = True
        prevLine = lines[lineIdx - 1]
        for idx in r:
          if(newNumber and prevLine[idx].isnumeric()):
            numbers.append(findNumber(prevLine, idx))
            newNumber = False
          elif(not prevLine[idx].isnumeric()):
            newNumber = True

      currentLine = lines[lineIdx]
      newNumber = True
      for idx in r:
        if(newNumber and currentLine[idx].isnumeric()):
          numbers.append(findNumber(currentLine, idx))
          newNumber = False
        elif(not currentLine[idx].isnumeric()):
          newNumber = True

      if((lineIdx + 1) <= 139):
        newNumber = True
        nextLine = lines[lineIdx + 1]
        for idx in r:
          if(newNumber and nextLine[idx].isnumeric()):
            numbers.append(findNumber(nextLine, idx))
            newNumber = False
          elif(not nextLine[idx].isnumeric()):
            newNumber = True
      
      if(len(numbers) == 2):
        count += int(numbers[0]) * int(numbers[1])
      
      

print(count)