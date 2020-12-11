import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
  lines = [l.strip() for l in f.readlines()]

modulus = len(lines[0])
hit = miss = 0

for row in range(len(lines)):
  col = row * 3
  result = lines[row][col % modulus]
  if result == '.':
    miss += 1
  elif result == '#':
    hit += 1
  else:
    print("error", result)

print(hit)