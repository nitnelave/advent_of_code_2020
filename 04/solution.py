import re

class Passport(object):
    def __init__(self):
        self.attr = set()
        self.valid_attr = set()

target_attributes = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
def validate_passport(passp):
    global target_attributes
    passp.attr.discard('cid')
    return passp.attr == target_attributes

def validate_passport_attr(passp):
    global target_attributes
    return passp.valid_attr == target_attributes

def validate_attribute(key, value):
    if key == 'byr':
        return re.fullmatch(r'\d{4}', value) and int(value) in range(1920, 2003)
    if key == 'iyr':
        return re.fullmatch(r'\d{4}', value) and int(value) in range(2010, 2021)
    if key == 'eyr':
        return re.fullmatch(r'\d{4}', value) and int(value) in range(2020, 2031)
    if key == 'hgt':
        return (re.fullmatch(r'\d{3}cm', value) and int(value[:3]) in range(150, 194)
                or re.fullmatch('\d{2}in', value) and int(value[:2]) in range(59, 77))
    if key == 'hcl':
        return re.fullmatch(r'#[0-9a-f]{6}', value)
    if key == 'ecl':
        return re.fullmatch(r'^(amb|blu|brn|gry|grn|hzl|oth)$', value)
    if key == 'pid':
        return re.fullmatch(r'\d{9}', value)
    return False


valid_passports = 0
valid_passports_attributes = 0
current_passport = Passport()

for l in open('input'):
    l = l.rstrip('\n')
    if l == '':
        valid_passports += validate_passport(current_passport)
        valid_passports_attributes += validate_passport_attr(current_passport)
        current_passport = Passport()
    else:
        for field in l.split(' '):
            key, value = field.split(':')
            current_passport.attr.add(key)
            if validate_attribute(key, value):
                current_passport.valid_attr.add(key)
validate_passport(current_passport)

print(valid_passports)
print(valid_passports_attributes)
