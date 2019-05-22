"""Knapsack

find the set of items to steal that will give you the most value.

can cary at most 4lb.
items:
  1lb - guitar - 1.5$
  3lb - laptop -  2$
  4lb - stereo -  3$

row - per distinct item, col - per distinct .lb

grid[row][col] = max (
  1. previous max - value at grid[row-1][col] , items up to current
          ---- or ----
    if current item's weight <= col (aka max allowed weight for the sub problem)
  2. current item value + maximum value for [remaining .lb]* aka grid[row-1][col - current item's .lb] 
  [remaining .lb] - max value for .lb without current item 
."""

import pprint

def get_max_value(items, weights, max_weight):
  rows = len(items) + 1
  cols = max_weight + 1
   
  dp = [[0 for _ in range(cols)] for _ in range(rows)]
  for row in range(1, rows):
    for col in range(1, cols):
      if col >= weights[row-1]:
        dp[row][col] = items[row-1] + dp[row-1][col - weights[row-1]]
      else:
        dp[row][col] = dp[row-1][col]

  pprint.pprint(dp, width=25)


get_max_value(items=[1.5, 2, 3], weights=[1, 2, 3], max_weight=4)