lines = open('../input.txt').read().splitlines()

cardRankings = {
  "J": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "T": 10,
  "Q": 11,
  "K": 12,
  "A": 13,
}

rounds = []

class Round:
  def __init__(self, hand, bid):
    self.hand = hand
    self.bid = bid
    self.matchingCards = []
    self.cardRanks = []

def getMatchingCards(r):
  cardDict = {}

  for card in r.hand:
    if card in cardDict:
      cardDict[card] += 1
    else:
      cardDict[card] = 1

  matchingCards = []
  for cardType in cardDict:
    if cardType != "J":
      matchingCards.append(cardDict[cardType])
  matchingCards.sort(reverse=True)

  if("J" in cardDict):
    if(len(matchingCards) > 0):
      matchingCards[0] += cardDict["J"]
    else:
      matchingCards.append(cardDict["J"])

  return matchingCards

for line in lines:
  lineParts = line.split(" ")
  r = Round(lineParts[0], int(lineParts[1]))

  for card in r.hand:
    r.cardRanks.append(cardRankings[card])

  r.matchingCards = getMatchingCards(r)
  
  rounds.append(r)

rounds = sorted(rounds, key=lambda self: self.cardRanks)
rounds = sorted(rounds, key=lambda self: self.matchingCards)

totalWinnings = 0
for rIdx, r in enumerate(rounds):
  totalWinnings += (r.bid * (rIdx + 1))

print(totalWinnings)