"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.
"""

import pprint

def CanBePartitioned(nums):
  nums_sum = sum(nums)
  if nums_sum % 2 != 0:
    return False

  target_sum = nums_sum // 2
  dp = [
    [0 for _ in range(target_sum + 1)]
    for _ in range(len(nums) + 1)
  ]

  for row in range(1, len(nums) +1):
    for col in range(1, (target_sum + 1)):
      if nums[row-1] <= col:
        cur = nums[row-1] + dp[row-1][(col - nums[row-1])]
        dp[row][col] = max(cur, dp[row-1][col])
      else:
        dp[row][col] =  dp[row-1][col]
  
  pprint.pprint(dp)
  return dp[-1][-1] == target_sum


CanBePartitioned([1, 5, 11, 5])