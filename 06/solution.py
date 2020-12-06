
groups = []
# Union, intersection of questions for a group.
questions = (set(), set())
for line in open('input'):
    line = line.rstrip('\n')
    if line == '':
        groups.append(questions)
        questions = (set(), set())
        continue
    if len(questions[0]) == 0:
        questions = (set(line), set(line))
    else:
        questions = (questions[0].union(line), questions[1].intersection(line))
groups.append(questions)

print(sum(len(x[0]) for x in groups))
print(sum(len(x[1]) for x in groups))
