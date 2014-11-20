# http://en.wikipedia.org/wiki/Zebra_Puzzle
import itertools

def on_right(h1, h2):
    return h1 - h2 == 1

def next_to(h1, h2):
    return abs(h1 - h2) == 1

def zebra_puzzle():
  houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
  orderings = list(itertools.permutations(houses))
  return next((WATER, ZEBRA)

    # Assign a color to each house
    for (red, green, ivory, yellow, blue) in c(orderings)

    # Is house1 to the right of house2?
    if on_right(green, ivory)

    # Assign each person to an ordering of houses
    for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)

    # Is the englisman in the red house?
    if Englishman is red

    # Is the norwegian in the first house?
    if Norwegian is first

    # Etc.
    if next_to(Norwegian, blue)
    for (coffee, tea, milk, oj, WATER) in c(orderings)
    if coffee is green
    if Ukranian is tea
    if milk is middle
    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
    if Kools is yellow
    if LuckyStrike is oj
    if Japanese is Parliaments
    for (dog, snails, fox, horse, ZEBRA) in c(orderings)
    if Spaniard is dog
    if OldGold is snails
    if next_to(Chesterfields, fox)
    if next_to(Kools, horse)
    )

def c(sequence):
  return sequence

print zebra_puzzle()

def ints(start, end = None):
  i = start
  while i <= end or end is None:
    yield i
    i = i + 1

def all_ints():
  "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
  yield 0
  for i in ints(1):
    yield i
    yield -i
