import math
import os
import sys

def load_input():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        cur_ts = int(f.readline().strip())
        buses = f.readline().strip().split(',')
        buses = [int(id) for id in buses if id != 'x']
    return (cur_ts, buses)

cur_ts, buses = load_input()

def wait_time(bus):
    return (math.ceil(cur_ts / bus) * bus) - cur_ts

next = min(buses, key=wait_time)
wait = wait_time(next)

print(next * wait)
