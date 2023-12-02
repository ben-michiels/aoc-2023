import re

redRegex = "(\d+) red"
greenRegex = "(\d+) green"
blueRegex = "(\d+) blue"

lines = open('../input.txt').read().splitlines()

count = 0

def findMax(regex, line):
  matches = re.findall(regex, line, re.MULTILINE)
  numbers = list(map(int, matches))
  numbers.sort()
  return max(numbers)

for line in lines:
  maxRed = findMax(redRegex, line)
  maxGreen = findMax(greenRegex, line)
  maxBlue = findMax(blueRegex, line)

  count = count + (maxRed * maxGreen * maxBlue)

print(count)