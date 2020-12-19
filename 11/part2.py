import os
import sys

FLOOR = '.'
EMPTY = 'L'
FULL = '#'

def initial_seats():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        seats = [[ch for ch in row.strip()] for row in f.readlines()]
    return seats

def initial_adjs(seats):
    return [[[[None] * 3, [None] * 3, [None] * 3]
            for col in seats[0]] for row in seats]

initial = initial_seats()
n_rows = len(initial)
n_cols = len(initial[0])

def next_seats(seats, adj, row, col):
    results = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if next_seat_full(seats, adj, row + dy, col + dx, dx, dy):
                results += 1
    return results

def next_seat_full(seats, adjs, row, col, dx, dy):
    if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
        return False
    if seats[row][col] != FLOOR:
        return seats[row][col] == FULL
    if adjs[row][col][dy + 1][dx + 1] is None:
        adjs[row][col][dy + 1][dx + 1] = next_seat_full(
                seats, adjs, row + dy, col + dx, dx, dy)
    return adjs[row][col][dy + 1][dx + 1]

def stable_seats():
    seats = initial
    while True:
        new_layout = [row[:] for row in seats]
        adjs = initial_adjs(new_layout)
        for row in range(0, n_rows):
            for col in range(0, n_cols):
                seat = seats[row][col]
                adj = next_seats(seats, adjs, row, col)
                if seat == EMPTY and adj == 0:
                    new_layout[row][col] = FULL
                if seat == FULL and adj > 4:
                    new_layout[row][col] = EMPTY
        if new_layout == seats:
            return seats 
        seats = new_layout

def total_full():
    return sum([row.count(FULL) for row in stable_seats()])

print(total_full())
