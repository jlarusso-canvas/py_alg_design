import itertools


def imright(h1, h2):
    return h1 - h2 == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle():
  houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
  orderings = list(itertools.permutations(houses))
  print orderings


zebra_puzzle()
