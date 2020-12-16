#! /usr/bin/env python3

import re, itertools, math

def parse_rule(r):
    m = re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', r)
    return (m.group(1), (range(int(m.group(2)), int(m.group(3)) + 1), range(int(m.group(4)), int(m.group(5)) + 1)))

rules, _, ticket, _, tickets = (list(g) for _, g in itertools.groupby(open('input'), key='\n'.__ne__))

rules = list(map(parse_rule, rules))
ticket = list(map(int, ticket[1].split(',')))
tickets = [list(map(int, t.split(','))) for t in tickets[1:]]

def rule_matches(r, i):
    return i in r[1][0] or i in r[1][1]

def match_any_rule(i):
    return any(map(lambda r: rule_matches(r, i), rules))

print(sum(itertools.filterfalse(match_any_rule, itertools.chain(*tickets))))

rules_per_pos = [set.intersection(
    *(set(i for i, r in enumerate(rules) if rule_matches(r, t[pos]))
        for t in tickets if all(map(match_any_rule, t))))
    for pos in range(len(ticket))]
found = set()
while len(found) < len(ticket):
    for i in range(len(rules_per_pos)):
        if i in found:
            continue
        if len(rules_per_pos[i]) == 1:
            found.add(i)
            el = next(iter(rules_per_pos[i]))
            for j in range(len(rules_per_pos)):
                if j == i:
                    continue
                rules_per_pos[j].discard(el)

name_per_pos = [rules[next(iter(i))][0] for i in rules_per_pos]
print(math.prod(ticket[i]
    for i, name in enumerate(name_per_pos) if name.startswith('departure')))
