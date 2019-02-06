"""Find all possible string permutations."""

def permute(string):
  if len(string) == 1:
    return string

  res = set()
  for i in range(len(string)):
    sub_str = string[:i] + string[i+1:]
    permutes = permute(sub_str)
    for p in permutes:
      res.add(string[i] + p)
  return res

print(permute('abc'))