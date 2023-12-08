from itertools import cycle
from math import lcm
from re import findall

commands, _, *nodeLines = open("../input.txt", "r").readlines()
nodeDict = dict((key, [left, right]) for (key, left, right) in map(lambda nodeLine: findall("[A-Z]+", nodeLine), nodeLines))                    

def followPaths():
    results = []
    for key in [nodeId for nodeId in nodeDict.keys() if nodeId.endswith("A")]:
        for index, command in enumerate(cycle(commands.strip()), 1):
            key = nodeDict[key][0 if command == "L" else 1]
            if key.endswith("Z"):
                results.append(index)
                break
    return lcm(*results)

print(followPaths())