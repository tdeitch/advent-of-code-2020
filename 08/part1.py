import os
import sys

boot = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
  for line in f:
    instruction, relnum = line.strip().split(" ")
    boot.append((instruction, relnum))

acc = 0
iptr = 0
seen = set()
while iptr not in seen:
  seen.add(iptr)
  cmd, arg = boot[iptr]

  if cmd == "jmp":
    iptr += int(arg)
  else:
    iptr += 1

  if cmd == "acc":
    acc += int(arg)

print(acc)