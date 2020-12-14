import re
import numpy as np

def parse_line(l):
    m = re.match(r'(.)(\d+)', l)
    return (m[1], int(m[2]))

commands = list(map(parse_line, open('input')))

def get_rotation(angle):
    return np.array({
            0:  [[1, 0], [0, 1]],
            90: [[0, 1], [-1, 0]],
            180: [[-1, 0], [0, -1]],
            270: [[0, -1], [1, 0]],
            }[((angle % 360) + 360) % 360])

def get_direction(axis):
    return np.array({
            'E':  (1, 0),
            'N': (0, 1),
            'W': (-1, 0),
            'S': (0, -1)
            }[axis])

def get_part1(commands):
    angle = 0
    pos = np.array((0, 0))
    east = np.array((1, 0))

    for c, v in commands:
        if c == 'L':
            angle -= v
        elif c == 'R':
            angle += v
        elif c == 'F':
            pos += v * np.matmul(get_rotation(angle), east)
        else:
            pos += v * get_direction(c)
    return pos

def get_part2(commands):
    angle = 0
    pos = np.array((0, 0))
    waypoint = np.array((10, 1))

    for c, v in commands:
        if c == 'L':
            waypoint = np.matmul(get_rotation(-v), waypoint)
        elif c == 'R':
            waypoint = np.matmul(get_rotation(v), waypoint)
        elif c == 'F':
            pos += v * waypoint
        else:
            waypoint += v * get_direction(c)
    return pos

print(sum(map(abs, get_part1(commands))))
print(sum(map(abs, get_part2(commands))))
