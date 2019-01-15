"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""

def get_single_num(nums):
  sinle = 0
  for num in nums:
    single ^= num
  return single