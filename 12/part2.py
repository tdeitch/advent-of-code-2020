import os
import sys

def load_steps():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return [(s[0], int(s[1:])) for s in f.readlines()]

def turn_left(cur_dir):
    return [-1 * cur_dir[1], cur_dir[0]]

def turn_right(cur_dir):
    return [cur_dir[1], -1 * cur_dir[0]]

steps = load_steps()
loc = [0, 0]
waypoint = [10, 1]

for action, dist in steps:
    if action == 'N':
        waypoint[1] += dist
    if action == 'S':
        waypoint[1] -= dist
    if action == 'E':
        waypoint[0] += dist
    if action == 'W':
        waypoint[0] -= dist
    if action == 'L':
        for _i in range(dist // 90):
            waypoint = turn_left(waypoint)
    if action == 'R':
        for _i in range(dist // 90):
            waypoint = turn_right(waypoint)
    if action == 'F':
        loc[0] += waypoint[0] * dist
        loc[1] += waypoint[1] * dist

print(abs(loc[0]) + abs(loc[1]))
