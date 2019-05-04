"""https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life."""

STATES = {'1': '1-1', '2': '0-1', '3': '1-0', '4': '0-0'}

def get_live_neighboors(board, row, col, rows, cols):
  count = 0
  for r in range(row-1, row+2):
    if r < 0 or r >= rows:
      continue
    for c in range(col-1, col+2):
      if c < 0 or c >= cols:
        continue
      if r == row and c == col:
        continue
      if board[r][c] == 1 or board[r][c] == 3:
        count += 1
  return count

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
      rows = len(board)
      cols = len(board[0])
      for r in range(rows):
        for c in range(cols):
          num_live_cells = get_live_neighboors(board, r, c, rows, cols)
          if board[r][c] == 1:
            if num_live_cells < 2 or num_live_cells > 3:
                board[r][c] = 3
      
          elif board[r][c] == 0:
            if num_live_cells == 3:
              board[r][c] = 2
            
      for r in range(rows):
        for c in range(cols):
          if 1 <= board[r][c] <= 2:
            board[r][c] = 1
          else:
            board[r][c] = 0
        



        
