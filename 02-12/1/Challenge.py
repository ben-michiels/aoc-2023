import re

redRegex = "(\d+) red"
greenRegex = "(\d+) green"
blueRegex = "(\d+) blue"

lines = open('../input.txt').read().splitlines()

count = 0

for index, line in enumerate(lines):
  redMatches = re.findall(redRegex, line, re.MULTILINE)
  if any(int(match) > 12 for match in redMatches):
    continue

  greenMatches = re.findall(greenRegex, line, re.MULTILINE)
  if any(int(match) > 13 for match in greenMatches):
    continue

  blueMatches = re.findall(blueRegex, line, re.MULTILINE)
  if any(int(match) > 14 for match in blueMatches):
    continue

  count = count + (index + 1)

print(count)