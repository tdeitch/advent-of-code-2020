import os
import sys

def load_program():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return [tuple(line.strip().split(" = ")) for line in f.readlines()]

def to_int(s):
    return int(s, base=2)

def to_str(i):
    return "{0:036b}".format(i)

def apply_ones_mask(ptr, mask):
    ptr = to_str(ptr)
    result = []
    for i in range(36):
        if mask[i] == "1":
            result.append("1")
        else:
            result.append(ptr[i])
    return to_int("".join(result))

def apply_xs_mask(ptr, mask):
    if "X" not in mask:
        return [ptr]
    idx = mask.index("X")
    mask = mask[:idx] + "0" + mask[idx+1:]
    ptr = to_str(ptr)
    ptr0 = to_int(ptr[:idx] + "0" + ptr[idx+1:])
    ptr1 = to_int(ptr[:idx] + "1" + ptr[idx+1:])
    return apply_xs_mask(ptr0, mask) + apply_xs_mask(ptr1, mask)

def apply_masks(ptr, mask):
    ptr = apply_ones_mask(ptr, mask)
    return apply_xs_mask(ptr, mask)

def run(program):
    mask = None
    mem = dict()
    for cmd, val in program:
        if cmd == "mask":
            mask = val
            continue
        ptr = int(cmd[4:-1])
        val = int(val)
        for new_ptr in apply_masks(ptr, mask):
            mem[new_ptr] = val
    return mem

program = load_program()
mem = run(program)
print(sum(mem.values()))
