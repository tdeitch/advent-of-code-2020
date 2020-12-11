import os
import sys

def load():
  pws = []
  with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f.readlines():
      length, letter, pw = line.strip().split(" ")
      letter = letter[0]
      p1, p2 = (int(x) for x in length.split("-"))
      pws.append((p1, p2, letter, pw))
  return pws

def matches(policy):
  p1, p2, letter, pw = policy
  return (pw[p1-1] == letter) != (pw[p2-1] == letter)

good_pws = [pw for pw in load() if matches(pw)]
print(len(good_pws))