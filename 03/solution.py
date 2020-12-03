import math
trees = [[x == '#' for x in l if x in '.#'] for l in open('input')]

def tree_for_slope(x, y):
    num_trees = 0
    for i in range(1, len(trees)):
        if x * i >= len(trees):
            break
        if trees[x * i][(y*i) % len(trees[0])]:
            num_trees += 1
    return num_trees

print(tree_for_slope(1, 3))

print(math.prod(tree_for_slope(x, y) for (x, y) in
    [(1, 1),
     (1, 3),
     (1, 5),
     (1, 7),
     (2, 1)]))
