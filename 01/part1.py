import json
import os
import sys

s = 2020
with open(os.path.join(sys.path[0], 'data.json')) as f:
  ns = json.load(f)
for ai, a in enumerate(ns):
  b = s - a
  if b in ns[ai+1:]:
    print(a*b)