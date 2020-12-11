import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
  passes = [l.strip() for l in f.readlines()]

def decode(s, zero, one):
  n = ""
  for ch in s:
    if ch == zero:
      n = n + "0"
    elif ch == one:
      n = n + "1"
    else:
      print("Error")
  return int(n, base=2)

def seat_id(s):
  row = decode(s[:7], "F", "B")
  col = decode(s[7:], "L", "R")
  return row * 8 + col

print(max([seat_id(p) for p in passes]))