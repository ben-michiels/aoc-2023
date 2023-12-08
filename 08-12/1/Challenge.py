from itertools import cycle
from re import findall

commands, _, *nodeLines = open("../input.txt", "r").readlines()
nodeDict = dict((key, [left, right]) for (key, left, right) in map(lambda nodeLine: findall("[A-Z]+", nodeLine), nodeLines))                    

def followPath():
    key = "AAA"
    for index, command in enumerate(cycle(commands.strip()), 1):
        key = nodeDict[key][0 if command == "L" else 1]
        if key == "ZZZ":
            return index

print(followPath())