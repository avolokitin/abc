"""Insertion Sort

1. Efficient for (quite) small data sets
2. efficient for data sets that are already substantially sorted
3. only requires a constant amount O(1) of additional memory space
"""
import pprint 

def insertion_sort(array):
  """for each elem in a list
    
  shift all elements < elem at index to the left."""  

  for index in range(1, len(array)):
    pos = index
    pivot = array[index]

    while pos > 0 and array[pos-1] > pivot:
       array[pos] = array[pos-1]
       pos -= 1
    array[pos] = pivot
  return array


array = [3, 1, 2, 0, 4]
assert sorted(array) == insertion_sort(array)
pprint.pprint(array)

# or to insert elems in sorted order
import bisect
import random

array = []
array2 = []
for num in range(10):
  rand_num = random.randint(0,100)
  array2.append(rand_num)
  # insert in sorted fashion , keep dup to the left
  bisect.insort_left(array, rand_num)
  
assert sorted(array2) == array
pprint.pprint(array)