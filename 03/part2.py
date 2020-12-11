import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
  lines = [l.strip() for l in f.readlines()]

modulus = len(lines[0])

def hits_for_slope(rows_down, cols_over):
  hit = miss = 0
  for row in range(0, len(lines), rows_down):
    col = row // rows_down * cols_over
    result = lines[row][col % modulus]
    if result == '.':
      miss += 1
    elif result == '#':
      hit += 1
    else:
      print("error", result)
  return hit

a = hits_for_slope(1, 1)
b = hits_for_slope(1, 3)
c = hits_for_slope(1, 5)
d = hits_for_slope(1, 7)
e = hits_for_slope(2, 1)

print(a*b*c*d*e)