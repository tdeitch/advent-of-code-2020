import os
import sys

FLOOR = '.'
EMPTY = 'L'
FULL = '#'

def initial_seats():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        seats = [[ch for ch in row.strip()] for row in f.readlines()]
    return seats

def add_border(seats):
    seats.insert(0, [FLOOR for _i in range(len(seats[0]))])
    seats.append([FLOOR for _i in range(len(seats[0]))])
    for row in seats:
        row.insert(0, FLOOR)
        row.append(FLOOR)
    return seats

initial = add_border(initial_seats())
n_rows = len(initial)
n_cols = len(initial[0])

def adj_full(seats, row, col):
    results = 0
    if seats[row][col] == FULL:
        results -= 1
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if seats[i][j] == FULL:
                results += 1
    return results

def stable_seats():
    seats = initial
    while True:
        new_layout = [row[:] for row in seats]
        for row in range(1, n_rows - 1):
            for col in range(1, n_cols - 1):
                seat = seats[row][col]
                adj = adj_full(seats, row, col)
                if seat == EMPTY and adj == 0:
                    new_layout[row][col] = FULL
                if seat == FULL and adj > 3:
                    new_layout[row][col] = EMPTY
        if new_layout == seats:
            return seats 
        seats = new_layout

def total_full():
    return sum([row.count(FULL) for row in stable_seats()])

print(total_full())
