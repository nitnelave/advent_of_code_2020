#! /usr/bin/env python

import numpy as np

initial = list(map(lambda l: l.rstrip('\n'), open('input')))

def compute_cell(grid, i, j, k, l):
    count = -int(grid[i][j][k][l])
    for a in range(-1, 2):
        for b in range(-1, 2):
            for c in range(-1, 2):
                for d in range(-1, 2):
                    count += grid[i + a][j + b][k + c][l + d]
    return count == 3 or (count == 2 and grid[i][j][k][l])


def compute_step(grid, offset, turn, four_dim):
    new_grid = np.zeros_like(grid)
    for i in range(offset - turn - 1, offset + len(initial) + turn + 1):
        for j in range(offset - turn - 1, offset + len(initial[0]) + turn + 1):
            for k in range(offset - turn - 1, offset + 1 + turn + 1):
                for l in range(offset - turn - 1, offset + 1 + turn + 1) if four_dim else range(1, 2):
                    new_grid[i][j][k][l] = compute_cell(grid, i, j, k, l)
    return new_grid

def simulate_game_of_life(turns, four_dim=False):
    turns = turns + 1
    width = len(initial) + 2 * turns
    height = len(initial[0]) + 2 * turns
    depth = 1 + 2 * turns
    girth = depth if four_dim else 3
    grid = np.zeros((width, height, depth, girth), dtype=bool)
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            grid[i + turns][j + turns][turns][girth // 2] = initial[i][j] == '#'

    for t in range(turns - 1):
        grid = compute_step(grid, turns, t, four_dim)

    print(np.sum(grid))



simulate_game_of_life(6)
simulate_game_of_life(6, True)
