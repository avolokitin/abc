"""
Write a function that takes a string as input and returns the string reversed.

Example 1:
Input: "hello"
Output: "olleh"

Example 2:
Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


def reverse(string):
  length = len(string)
  last = length // 2
  previous = -1
  result = list(string)
  for index in range(0, last):
    result[index], result[previous] = result[previous], result[index]
    previous -= 1
  return ''.join(result)

