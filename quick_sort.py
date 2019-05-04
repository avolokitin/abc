"""Quick sort implementation."""


def QuickSortRec(nums):
  """."""

  if len(nums) <= 1:
    return nums

  pivot = nums[0]
  lesser = []
  greater = []
  pivots = []

  for num in nums:
    if num < pivot:
      lesser.append(num)
    elif num > pivot:
      greater.append(num)
    else:
      pivots.append(num)

  return QuickSortRec(lesser) + pivots + QuickSortRec(greater)



print(QuickSortRec([1, 3, 2, 3, 5]))