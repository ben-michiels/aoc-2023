import re
from functools import cache
from functools import reduce

rows = open('../input.txt').read().splitlines()

allPossibilities = 0

@cache
def findPossibilities(record, numbers, possibilities = 0):
  minSpacesRequired = reduce(lambda a, b: a + b + 1, numbers)
  for idx, char in enumerate(record):
    if(len(record) < idx + minSpacesRequired):
      break
    if(char == "."):
      continue
    if(record[:idx].count("#") > 0):
      break

    spaces = record[idx:(idx + numbers[0])]
    afterSpaces = None if len(record) <= (idx + numbers[0]) else record[idx + numbers[0]]

    if(all(space != "." for space in spaces) and afterSpaces != "#"):
      if(len(numbers) == 1):
        if(all(space != "#" for space in record[idx + numbers[0]:])):
          possibilities += 1
      else:
        possibilities += findPossibilities(record[idx + numbers[0] + 1:], numbers[1:])
  return possibilities

for row in rows:
    record, numberString = row.split()
    numbers = tuple(map(int, re.findall("\d+", row)))
    possibilities = findPossibilities(record, numbers)

    allPossibilities += possibilities

print(allPossibilities)
