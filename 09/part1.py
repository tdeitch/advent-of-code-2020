import os
import sys

def possible_sums(ns):
    return set(n1 + n2 for n1 in ns for n2 in ns if n1 != n2)

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    nums = [int(line.strip()) for line in f.readlines()]

for i, num in enumerate(nums[25:]):
    preamble = nums[i:i+25]
    sums = possible_sums(preamble)
    if num not in sums:
        print(num)
        break

