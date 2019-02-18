"""Given a string with parenthesis, eliminate the illegal parenthesis and return a legal string.

Order must be saved
For example: 
 "(()" -&gt; "()"
 ")))(" -&gt; "" 
 "()(()" -&gt; "()()"
 "(())()" - "(())()"
"""

def get_valid_parentheses(string):
  openning = []
  valid = set()

  for index, char in enumerate(string):
    if char == '(':
      openning.append(index)
    else:
      if openning:
        left = openning.pop()
        valid.add(left)
        valid.add(index)
  
  res = []
  for index in range(len(string)):
    if index in valid:
      res.append(string[index])
  return ''.join(res)

print(get_valid_parentheses('(())()'))


