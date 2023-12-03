lines = open('../input.txt').read().splitlines()

count = 0

def isSymbol(line, idx):
  if(idx < 0 or idx >= 140):
    return False
  char = line[idx]
  return char.isnumeric() == False and char != "."

def isPart(lineIdx, start, end):
  isPart = False
  r = range(start, end + 1)

  if((lineIdx - 1) >= 0):
    prevLine = lines[lineIdx - 1]
    for idx in r:
      if(isSymbol(prevLine, idx)):
        return True

  currentLine = lines[lineIdx]
  if(isSymbol(currentLine, start) or isSymbol(currentLine, end)):
    return True
  
  if((lineIdx + 1) <= 139):
    nextLine = lines[lineIdx + 1]
    for idx in r:
      if(isSymbol(nextLine, idx)):
        return True

for lineIdx, line in enumerate(lines):
  currentNumber = ""
  start = 0
  end = 0

  for charIdx, char in enumerate(line):
    if(char.isnumeric()):
      currentNumber += char
      if(len(currentNumber) == 1):
        start = charIdx - 1
      if(charIdx == 139 or line[charIdx + 1].isnumeric() == False):
        end = charIdx + 1
        if(isPart(lineIdx, start, end)):
          count += int(currentNumber)
          print(currentNumber)
        currentNumber = ""
      
print(count)