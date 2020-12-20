import os
import sys

def load_program():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return [tuple(line.strip().split(" = ")) for line in f.readlines()]

def apply_mask(val, mask):
    val = "{0:036b}".format(val)
    result = []
    for i in range(36):
        if mask[i] == "0":
            result.append("0")
        if mask[i] == "1":
            result.append("1")
        if mask[i] == "X":
            result.append(val[i])
    return int("".join(result), base=2)

def run(program):
    mask = None
    mem = dict()
    for cmd, val in program:
        if cmd == "mask":
            mask = val
            continue
        ptr = int(cmd[4:-1])
        val = int(val)
        new_val = apply_mask(val, mask)
        mem[ptr] = new_val
    return mem

program = load_program()
mem = run(program)
print(sum(mem.values()))
