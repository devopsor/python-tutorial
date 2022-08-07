#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(range(1, 11))  #range(1, 11)
print(list(range(1, 11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n')

# But what if you want to generate [1x1, 2x2, 3x3, ..., 10x10]it? The first method is to loop:
L = []
for x in range(1, 11):
    L.append(x * x)
print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('\n')

#But the loop is too cumbersome, and the list comprehension can replace the loop with one line 
# to generate the above list:
print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ']) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()]) # ['x=A', 'y=B', 'z=C']

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L]) # ['hello', 'world', 'ibm', 'apple']

