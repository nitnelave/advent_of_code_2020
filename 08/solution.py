def parse_instr(line):
    op, val = line.split(' ')
    return (op, int(val))


# map of instruction -> increment in pic, acc
instructions = {
        'acc': lambda v: (1, v),
        'jmp': lambda v: (v, 0),
        'nop': lambda v: (1, 0),
        }

program = list(map(parse_instr, open('input')))

def run_program():
    acc = 0 # accumulator
    pic = 0 # Program Instruction Counter
    seen_instr = set()
    while True:
        # Correct end.
        if pic == len(program):
            return acc, True
        # Invalid end: infinite loop or out-of-bounds
        if pic in seen_instr or pic < 0 or pic > len(program):
            return acc, False
        seen_instr.add(pic)
        op, val = program[pic]
        pp, pa = instructions[op](val)
        acc += pa
        pic += pp

def toggle_nop_jmp(s):
    if s == 'nop':
        return 'jmp'
    return 'nop'

print(run_program()[0])

for i in range(len(program)):
    op, val = program[i]
    if op in ('jmp', 'nop'):
        program[i] = (toggle_nop_jmp(op), val)
        acc, success = run_program()
        if success:
            print(acc)
            break
        program[i] = (op, val)

