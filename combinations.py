"""."""

def getUniqueCombinations(alist, numb):
  for i in range(len(alist)):
    if numb==1:
      yield alist[i]
    else:
      for combo in getUniqueCombinations(alist[i+1:], numb-1):
        yield alist[i] + combo


"abc" 'ab' 'ac' 'bc' 

