import functools

timestamp, input = open('input')
input = input.rstrip('\n').split(',')
# List of bus numbers.
buses = [int(bus) for bus in input if bus != 'x']

wait_times = [i - (int(timestamp) % i) for i in buses]
min_wait = min(wait_times)
print(buses[wait_times.index(min_wait)] * min_wait)

# List of (bus period, modulo). Note the negative.
constraints = [(int(b), -i % int(b)) for i, b in enumerate(input) if b != 'x']

def combine_constraints(c1, c2):
    m1, r1 = c1
    m2, r2 = c2
    # Magic
    # JK :D. There is k1, k2 such that:
    # x = m1 * k1 + r1 = m2 * k2 + r2
    # m1 * k1 = m2 * k2 + r2 - r1
    # m1 * k1 = r1 - r1 [mod m2]
    # k1 = m1^-1 * (r1 - r1) [mod m2] where m1^-1 is the modular multiplicative inverse.
    # By replacing that in the first equation, we get:
    # There is k3 such that:
    # x = m1 * (m1^-1 * (r2 - r1) + k3) + r1
    #   = m1 * m1^-1 * (r2 - r1) + r1 + k3 * m1 * m2
    # Which combines both constraints into 1.
    # The modular multiplicative inverse of m1 mod m2 is given by pow(m1, -1, m2).
    return (m1 * m2, (m1 * pow(m1, -1, m2) * (r2 - r1) + r1))

constraint = functools.reduce(combine_constraints, constraints, (1, 0))
# Take the smallest positive one.
print(constraint[1] % constraint[0])
