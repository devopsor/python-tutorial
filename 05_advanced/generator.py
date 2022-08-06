#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s) #<generator object <genexpr> at 0x0000016CF7B77CF0>
for x in s:
    print(x)
# 0
# 1
# 4
# 9
# 16


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)  #fib(10): <generator object fib at 0x0000016CF7C33350>
for x in f:
    print(x)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# Generator return value: done
