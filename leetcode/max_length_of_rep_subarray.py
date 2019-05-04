"""."""

import pprint

def findLength(A, B) -> int:
    rows = len(A) + 1
    columns = len(B) + 1
    mx = [([0] * rows) for _ in range(columns)]
    
    for column in range(1, columns):
        for row in range(1, rows):
            if A[row-1] == B[column-1]:
                mx[column][row] = mx[column-1][row-1] + 1
    max_column = max(max(column) for column in mx)
    pprint.pprint(mx, width=25)


findLength([1,2,3],
           [1,2,3])