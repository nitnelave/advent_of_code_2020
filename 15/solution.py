#! /usr/bin/env python

numbers = list(map(int, next(open('input')).split(',')))

def compute_turn(numbers, target_turn):
    last_mention = [-1] * target_turn
    for i, c in enumerate(numbers[:-1]):
        last_mention[c] = i
    last_number = numbers[-1]
    for i in range(len(numbers) - 1, target_turn - 1):
        prev = last_mention[last_number]
        if prev == -1:
            next_number = 0
        else:
            next_number = i - prev
        last_mention[last_number] = i
        last_number = next_number
    return last_number

print(compute_turn(numbers, 2020))
print(compute_turn(numbers, 30000000))
