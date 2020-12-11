#! /usr/bin/env python
import copy

# Pad the list on all sides with empty seats that will never be filled.
# That saves us from checking bounding boxes.
seats = [list('L' + l.rstrip('\n') + 'L') for l in open('input')]
seats = [['L'] * len(seats[0])] + seats + [['L'] * len(seats[0])]


# s is the seat layout.
# distant is whether we consider distant seats or only immediat neighbors.
# n is the max number of neighbors we tolerate.
def too_many_neighbors(s, distant, x, y, n):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            k = 1
            while True:
                seat = s[i*k + x][j*k + y]
                if seat != '.' or not distant:
                    count += (seat == '#')
                    if count > n:
                        return True
                    break
                k += 1
    return False

def stable_seats(s, distant_neighbors, tolerance):
    diff = 1
    while diff != 0:
        diff = 0
        output = [l.copy() for l in s]
        for i in range(1, len(s) - 1):
            for j in range(1, len(s[0]) - 1):
                seat = s[i][j]
                if seat == '.':
                    continue
                if seat == 'L' and not too_many_neighbors(s, distant_neighbors, i, j, 0):
                    diff += 1
                    output[i][j] = '#'
                if seat == '#' and too_many_neighbors(s, distant_neighbors, i, j, tolerance - 1):
                    diff += 1
                    output[i][j] = 'L'
        s = output
    return sum(l.count('#') for l in s)

print(stable_seats(seats, False, 4))
print(stable_seats(seats, True, 5))

