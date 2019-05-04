"""Reverse chars in words, preserving words order."""

string = 'Python is awesome !'

def reverse_order(itr):
  length = len(itr)
  last = length - 1
  itr = list(itr)
  for i in range(length//2):
    itr[i], itr[last] = itr[last], itr[i]
    last -= 1
  return itr

reversed_string = ''.join(reverse_order(string))
words = reversed_string.split()
print(' '.join(reverse_order(words)))