"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
def isValid(self, s):
  """
  :type s: str
  :rtype: bool
  """
  if len(s) % 2 != 0:
    return False
  openning = {'(', '{', '['}
  valid = {'{}', '()', '[]'}
  cur = []
    
  for char in s:
    if char in openning:
      cur.append(char)
    else:
      if not cur:
        return False
      left = cur.pop()
      if not (left + char) in valid:
        return False

  return len(cur) == 0
                    