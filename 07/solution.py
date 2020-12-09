from collections import defaultdict
import re

def parse_rule(line):
    color, contents = re.fullmatch(r'(.+) bags contain (.+).\n', line).groups()
    if contents == 'no other bags':
        return (color, {})
    return (color, {c: int(n) for (n, c) in [re.fullmatch(r'(\d+) (.+) bags?', bag).groups() for bag in contents.split(', ')]})

rules = dict(map(parse_rule, open('input')))
reversed_rules = defaultdict(set)
for color, contents in rules.items():
    for c in contents.keys():
        reversed_rules[c].add(color)

can_contain_shiny_gold = reversed_rules['shiny gold'].copy()
to_explore = can_contain_shiny_gold.copy()
explored = set()
while len(to_explore) != 0:
    c = to_explore.pop()
    explored.add(c)
    for container in reversed_rules[c]:
        can_contain_shiny_gold.add(container)
        if not container in explored:
            to_explore.add(container)

print(len(can_contain_shiny_gold))

def count_bag_content(color):
    count = 1
    for c, n in rules[color].items():
        count += n * count_bag_content(c)
    return count

print(count_bag_content('shiny gold') - 1)
