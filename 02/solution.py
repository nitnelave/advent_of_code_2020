import re

valid_passwords_range = 0
valid_passwords_pos = 0

for line in open('input'):
    lower, upper, letter, password = re.match(r"(\d+)-(\d+) (.): (.*)", line).groups()
    lower, upper = int(lower), int(upper)
    cnt = password.count(letter)
    valid_passwords_range += (cnt >= lower and cnt <= upper)
    valid_passwords_pos += ((password[lower - 1] == letter) ^ (password[upper - 1] == letter))

print(valid_passwords_range)
print(valid_passwords_pos)
