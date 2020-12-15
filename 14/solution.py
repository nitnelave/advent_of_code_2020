#! /usr/bin/env python

import re

def parse_instr(l):
    m = re.match(r'mask = ([01X]+)', l)
    if m is not None:
        return m.group(1)
    m = re.match(r'mem\[(\d+)\] = (\d+)', l)
    return (int(m.group(1)), int(m.group(2)))

instructions = list(map(parse_instr, open('input')))

def run_instructions_part1(instr):
    # int -> int
    memory = {}
    mask_or = 0 # contains the 1s
    mask_and = -1 # contains the 0s

    for i in instr:
        if isinstance(i, str):
            mask_or = int(i.replace('X', '0'), 2)
            mask_and = int(i.replace('X', '1'), 2)
        else:
            addr, val = i
            memory[addr] = (val | mask_or) & mask_and

    return sum(memory.values())

def write_with_floating_bits(mem, addr, val, floating_bits):
    if floating_bits == []:
        mem[addr] = val
        return
    write_with_floating_bits(mem, addr | (1 << floating_bits[0]), val, floating_bits[1:])
    write_with_floating_bits(mem, addr & ~(1 << floating_bits[0]), val, floating_bits[1:])

def run_instructions_part2(instr):
    # int -> int
    memory = {}
    mask_or = 0 # contains the 1s
    x_list = []

    for i in instr:
        if isinstance(i, str):
            mask_or = int(i.replace('X', '0'), 2)
            x_list = [35 - index for index, c in enumerate(i) if c == 'X']
        else:
            addr, val = i
            write_with_floating_bits(memory, addr | mask_or, val, x_list)

    return sum(memory.values())

print(run_instructions_part1(instructions))
print(run_instructions_part2(instructions))
