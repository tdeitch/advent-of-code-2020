import os
import sys

def load():
  pws = []
  with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f.readlines():
      length, letter, pw = line.strip().split(" ")
      letter = letter[0]
      minl, maxl = (int(x) for x in length.split("-"))
      pws.append((minl, maxl, letter, pw))
  return pws

def matches(policy):
  minl, maxl, letter, pw = policy
  ct = pw.count(letter)
  return minl <= ct <= maxl

good_pws = [pw for pw in load() if matches(pw)]
print(len(good_pws))