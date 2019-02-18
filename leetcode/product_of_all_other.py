""" Given an array nums of n integers where n > 1,  return an array output such that output[i]

is equal to the product of all the elements of nums except nums[i].

I.e nums = [2, 3, 5, 6] => [90, 60, 36, 30]
"""

def get_product(nums):
  before =[]
  after = []
  product = 1

  for num in nums:
    before.append(product)
    product *= num
  
  product = 1
  for index in range(len(nums)-1, -1, -1):
    after.insert(0, product)
    product *= nums[index]
  
  # product could be found in preciding loop
  for index, num in enumerate(after):
    before[index] *= num
  return before


print(get_product([2, 3, 5, 6]))