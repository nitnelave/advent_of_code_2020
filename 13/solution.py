import functools
timestamp, input = open('input')
input = input.rstrip('\n').split(',')
buses = [int(bus) for bus in input if bus != 'x']
constraints = [(int(b), -i % int(b)) for i, b in enumerate(input) if b != 'x']

wait_times = [i - (int(timestamp) % i) for i in buses]
min_wait = min(wait_times)
print(buses[wait_times.index(min_wait)] * min_wait)

def combine_constraints(c1, c2):
    m1, r1 = c1
    m2, r2 = c2
    # Magic
    return (m1 * m2, (m1 * pow(m1, -1, m2) * (r2 - r1) + r1))

constraint = functools.reduce(combine_constraints, constraints, (1, 0))
print(constraint[1] % constraint[0])
