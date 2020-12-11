import os
import sys

target = 552655238

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    nums = [int(line.strip()) for line in f.readlines()]

l = 0
r = 1

while sum(nums[l:r]) != target:
    if sum(nums[l:r]) < target:
        r += 1
    else:
        l += 1

print(min(nums[l:r]) + max(nums[l:r]))
