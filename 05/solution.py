import operator

def convert_seat(code):
    res = 0
    for l in code.rstrip('\n'):
        res = res * 2 + (l in 'BR')
    return res

seat_codes = sorted(map(convert_seat, open('input')))
print(seat_codes[-1])
print(seat_codes[list(map(operator.sub,
                          seat_codes[1:],
                          seat_codes[:-1])).index(2)] + 1)
