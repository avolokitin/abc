"""Rotate elems in a list."""


def rotate_right(lst, n):
  n = n % len(lst)
  rotated = [] 
  pivot_index = len(lst) - n
  for item in range(pivot_index, len(lst)):
    rotated.append(lst[item]) 
  for item in range(0, pivot_index):  
    rotated.append(lst[item]) 
  return rotated

print(rotate_right([1,2,3,4,5], 3))