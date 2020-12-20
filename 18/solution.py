#! /usr/bin/env python

import operator

exprs = list(open('input'))

def parse_num(l, start, recurs):
    #print(f'evaluate_num: start: {start}')
    if l[start] == '(':
        return recurs(l, start + 1)
    i = start
    res = 0
    while ord(l[i]) in range(ord('0'), ord('9') + 1):
        res = res * 10 + (ord(l[i]) - ord('0'))
        i += 1
    return res, i + (l[i] == ' ')

def parse_op(l, start):
    if l[start] == '*':
        return operator.mul, start + 2
    if l[start] == '+':
        return operator.add, start + 2

def parse_expr(l, start):
    #print(f'parse_expr: line: {l}, start: {start}')
    res, i = parse_num(l, start, parse_expr)
    while l[i] in '+*':
        op, i = parse_op(l, i)
        n, i = parse_num(l, i, parse_expr)
        res = op(res, n)
    if l[i] == ')':
        i += 1 + (l[i + 1] == ' ')
    return res, i

def parse_sum(l, start):
    res, i = parse_num(l, start, parse_mul)
    while l[i] in '+':
        op, i = parse_op(l, i)
        n, i = parse_num(l, i, parse_mul)
        res = op(res, n)
    #print(f'sum: {l[start:i]}')
    return res, i

def parse_mul(l, start):
    res, i = parse_sum(l, start)
    while l[i] in '*':
        op, i = parse_op(l, i)
        n, i = parse_sum(l, i)
        res = op(res, n)
    #print(f'mul: {l[start:i]}')
    if l[i] == ')':
        i += 1 + (l[i + 1] == ' ')
    return res, i


def evaluate_line(l):
    res = parse_expr(l, 0)[0]
    return res

def evaluate_line_reverse_prec(l):
    res = parse_mul(l, 0)[0]
    return res

print(sum(map(evaluate_line, exprs)))
print(sum(map(evaluate_line_reverse_prec, exprs)))
