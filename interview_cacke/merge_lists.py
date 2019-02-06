""" Merge two sorted arrays.

list1 = [3, 4, 6, 10, 11, 15]
list2 = [1, 5, 8, 12, 14, 19]
print merge_lists(list1, list2)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
."""

def merge_lists(l1, l2):
  res = []
  i = 0
  j = 0

  while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
      res.append(l1[i])
      i += 1
    elif l1[i] > l2[j]:
      res.append(l2[j])
      j += 1

  if i < (len(l1) - 1):
    res.extend(l1[i:])
  if j < (len(l2) - 1):
    res.extend(l2[j:])
  return res
  
print(merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))
