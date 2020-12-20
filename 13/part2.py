import math
import os
import sys

from chinese_remainder import chinese_remainder

def load_input():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        cur_ts = int(f.readline().strip())
        buses = f.readline().strip().split(',')
    return (cur_ts, buses)

def departure_requirement(i, bus):
    return i - (i // bus) * bus

def compute_requirements(buses):
    reqs = []
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        reqs.append((int(bus), departure_requirement(i, int(bus))))
    return reqs

def compute_mod_equations(reqs):
    mods = []
    for bus, req in reqs:
        mods.append((bus, 0 if req == 0 else bus - req))
    return mods

buses = load_input()[1]
reqs = compute_requirements(buses)
mods = compute_mod_equations(reqs)
ns = [m[0] for m in mods]
bs = [m[1] for m in mods]

print(chinese_remainder(ns, bs))
