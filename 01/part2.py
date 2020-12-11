import json
import os
import sys

s = 2020
with open(os.path.join(sys.path[0], 'data.json')) as f:
  ns = json.load(f)
ns.sort()
for ai, a in enumerate(ns):
  for bi, b in enumerate(ns[ai+1:]):
    c = s - a - b
    if c in ns[ai+bi+1:]:
      print(a*b*c)