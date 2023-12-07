lines = open('../input.txt').read().splitlines()

cardRankings = {
  "2": 1,
  "3": 2,
  "4": 3,
  "5": 4,
  "6": 5,
  "7": 6,
  "8": 7,
  "9": 8,
  "T": 9,
  "J": 10,
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
    matchingCards.append(cardDict[cardType])
  matchingCards.sort(reverse=True)

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