import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    adapters = [int(v.strip()) for v in f.readlines()]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

paths = {max(adapters): 1}

def n_paths(start):
    if start not in paths:
        if start not in adapters:
            paths[start] = 0
        else:
            paths[start] = sum([
                n_paths(start + 1),
                n_paths(start + 2),
                n_paths(start + 3)])
    return paths[start]

print(n_paths(0))
