import re

winningNumberRegex = ":([^|]+)"
entryRegex = "\| (.+)"

lines = open('../input.txt').read().splitlines()

count = len(lines)

def findMatchingMembers(array1, array2):
  matches = list([])

  for member in array1:
    if member in array2: matches.append(member)
  
  return matches

def getMatches(line):
  winningNumbers = re.findall(winningNumberRegex, line)[0].strip().split()

  entries = re.findall(entryRegex, line)[0].split()

  return len(findMatchingMembers(entries, winningNumbers))

def getCascadingCopies(lineIdx, matches):
  copies = matches
  r = range(lineIdx + 1, lineIdx + 1 + matches if lineIdx + 1 + matches <= 199 else 199)

  for idx in r:
    newMatches = getMatches(lines[idx])
    copies += getCascadingCopies(idx, newMatches)

  return copies

for lineIdx, line in enumerate(lines):
  matches = getMatches(line)

  if(matches > 0):
    count += getCascadingCopies(lineIdx, matches)

print(count)