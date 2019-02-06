"""
Given a list, return a list where each index stores the product of all numbers in the list except the number at the index itself.

The algorithm for this solution is to first create a new list with products
of all elements to the left of each element, then multiply each element in that list
to the product of all the elements to the right of the list by traversing it in reverse.
"""
def find_product(lst):
  left = 1
  product = []
  for ele in lst:
    product.append(left)
    left = left * ele
    
  right = 1
  for i in range(len(lst)-1,-1,-1):
    product[i] = product[i] * right
    right = right * lst[i]
    
  return product

print(find_product([0,1,2,3]))