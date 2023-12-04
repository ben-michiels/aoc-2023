import re

winningNumberRegex = ":([^|]+)"
entryRegex = "\| (.+)"

lines = open('../input.txt').read().splitlines()

count = 0

def findMatchingMembers(array1, array2):
  matches = list([])

  for member in array1:
    if member in array2: matches.append(member)
  
  return matches

for line in lines:
  winningNumbers = re.findall(winningNumberRegex, line)[0].strip().split()

  entries = re.findall(entryRegex, line)[0].split()

  matches = len(findMatchingMembers(entries, winningNumbers))

  if(matches > 0):
    count += 2 ** (matches - 1)

print(count)