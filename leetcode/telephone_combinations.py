"""

The backtracking algorithm traverses the search tree recursively, from the root down,
in depth-first order. At each node c, the algorithm checks whether c can be completed
to a valid solution. If it cannot, the whole sub-tree rooted at c is skipped (pruned).
Otherwise, the algorithm checks whether c itself is a valid solution,
and if so reports it to the user; and recursively enumerates all sub-trees of c.
The two tests and the children of each node are defined by user-given procedures.

Depth-first search (DFS) starts at the root (selecting some arbitrary node as the root
in the case of a graph) and explores as far as possible along each branch before
backtracking.

."""

class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    digit_to_letters = {
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h', 'i'],
      '5': ['j', 'k', 'l'],
      '6': ['m', 'n', 'o'],
      '7': ['p', 'q', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y', 'z']}
      
    def _dfs(res, index, digits, path):
        if len(path) == len(digits):
          res.append(path)
      
        for index in range(index, len(digits)):
          digit = digits[index]
          letters = digit_to_letters.get(digit)
          for letter in letters:
              _dfs(res, index+1, digits, path+letter)
    res = []
    _dfs(res, 0, digits, '')
    return res if res[0] else []
            