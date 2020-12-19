import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    adapters = [int(v.strip()) for v in f.readlines()]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

diffs = [0, 0, 0, 0]

for i in range(1, len(adapters)):
    low = adapters[i-1]
    high = adapters[i]
    diffs[high-low] += 1

print(diffs[1] * diffs[3])
