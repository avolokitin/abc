"""Binary Search."""

def BinarySearch(nums: int, target: int) -> int:
  """."""
  length = len(nums)
  pivot = length // 2
  left = 0
  right = length - 1
  
  while left < right:

    if nums[pivot] == target:
      return pivot
    
    if nums[pivot] < target:
      left += 1
    elif nums[pivot] > target:
      right -= 1
    
    pivot = left + right // 2
  
  return -1

def BinarySearchRec(nums: int, target: int, left: int, right:int) -> int:

  pivot = left + right // 2
  if nums[pivot] == target:
    return pivot
  
  return BinarySearchRec(nums, target, left+1, right-1)


print(BinarySearch([1,2, 6, 7, 11], 11))
print(BinarySearchRec([1,2, 6, 7, 11], 11, 0, 4))

