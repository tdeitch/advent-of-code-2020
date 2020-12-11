import os
import sys

orig_boot = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
  for line in f:
    instruction, relnum = line.strip().split(" ")
    orig_boot.append((instruction, relnum))

def terminates(boot, iptr, seen=set()):
  if iptr in seen:
    return False
  if iptr == 629:
    return True
  cmd, arg = boot[iptr]
  if cmd == "jmp":
    return terminates(boot, iptr + int(arg), seen | {iptr})
  return terminates(boot, iptr + 1, seen | {iptr})

def execute(boot):
  acc = 0
  iptr = 0
  while iptr != 629:
    cmd, arg = boot[iptr]
    if cmd == "jmp":
      iptr += int(arg)
    else:
      iptr += 1
    if cmd == "acc":
      acc += int(arg)
  return acc

for i in range(len(orig_boot)):
  new_boot = list(orig_boot)
  cmd, arg = new_boot[i]
  if cmd == "jmp":
    new_boot[i] = ("nop", arg)
  if cmd == "nop":
    new_boot[i] = ("jmp", arg)
  if terminates(new_boot, 0):
    print(execute(new_boot))
