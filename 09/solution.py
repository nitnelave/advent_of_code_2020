from collections import defaultdict

puzzle = list(map(int, open('input')))
preamble_size = 25

def sum_is_in_preamble(preamble, num):
    for n, c in preamble.items():
        if n + n == num:
            if c >= 2:
                return True
        else:
            if (num - n) in preamble:
                return True
    return False

def find_invalid_number():
    # {num -> #instances in preamble}
    # Entries with count 0 are cleared for fast iteration.
    preamble = defaultdict(int)
    for n in puzzle[:preamble_size]:
        preamble[n] += 1

    for i in range(preamble_size, len(puzzle)):
        if not sum_is_in_preamble(preamble, puzzle[i]):
            return puzzle[i]
        # Add the current number to the preamble.
        preamble[puzzle[i]] += 1
        # Remove the first preamble element.
        first_preamble = puzzle[i - preamble_size]
        preamble[first_preamble] -= 1
        if preamble[first_preamble] == 0:
            del(preamble[first_preamble])

invalid_num = find_invalid_number()
print(invalid_num)

# start and stop (exclusive) of the range that sums to invalid_num.
start, stop = 0, 1
sum = puzzle[0]
while sum != invalid_num:
    if sum > invalid_num:
        sum -= puzzle[start]
        start += 1
    else:
        sum += puzzle[stop]
        stop += 1

print(min(puzzle[start:stop]) + max(puzzle[start: stop]))
