#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python has built-in map() and reduce() functions.
# Let's look at the map first. 
# map() The function receives two parameters, 
# one is the function,           (※)
# and the other is Iterable,  (※)
# map the incoming function is applied to each element (※) of the sequence in turn, 
# and the result is Iteratorreturned as a new one.
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r) #<map object at 0x00000259EDAA1CA0>

l = list(r) 
print(l)  #[1, 4, 9, 16, 25, 36, 49, 64, 81]
print('\n')

l = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    l.append(f(n))
print(l) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# map function
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))




