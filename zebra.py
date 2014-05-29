import itertools


def on_right(h1, h2):
    return h1 - h2 == 1


def next_to(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle():
  houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
  orderings = list(itertools.permutations(houses))
  return next((WATER, ZEBRA)
    for (red, green, ivory, yellow, blue) in c(orderings)
    if on_right(green, ivory)
    for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
    if Englishman is red
    if Norwegian is first
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
