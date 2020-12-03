import re

valid_passwords_range = 0
valid_passwords_pos = 0

for l in open('input'):
    m = re.match(r"(\d+)-(\d+) (.): (.*)", l)
    if m is None:
        print(f"No match: {l}")
        continue
    lower, upper, letter, password = m.groups()
    lower = int(lower)
    upper = int(upper)
    cnt = password.count(letter)
    if cnt >= lower and cnt <= upper:
        valid_passwords_range += 1
    if (password[lower - 1] == letter) ^ (password[upper - 1] == letter):
        valid_passwords_pos += 1

print(valid_passwords_range)
print(valid_passwords_pos)
