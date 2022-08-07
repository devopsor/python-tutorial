#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reduce
# When a function is applied to a sequence [x1, x2, x3, ...], 
# the function must receive two parameters, 
# and reduce the result continues to be accumulated(※) with the next element of the sequence. 
# The effect is:
############### reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)###################

# For example, to sum a sequence, you can use reduce:
from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [1,2,3,4,5]))   #15
print('\n')

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))  #13579
print('\n')

# This example itself is not very useful, but if we consider that a string stris also a sequence, 
# and with a slight modification to the above example map(), 
# we can write a function that strconverts to int


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579'))) #13579
print(reduce(fn, list(map(char2num, '13579')))) #13579
print('\n')

#Arranged into a str2int function is:
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))
print(str2int(digits))  #123456789
print('\n')

# It can also be further simplified with a lambda function to:
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return digits[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int(digits))  #123456789
print('\n')

names = ['adam', 'LISA', 'barT']
def lowercase(name):
    fSlice = name[:1]
    lSlice = name[1:len(name)]
    return fSlice.upper() + lSlice.lower()
nameList = list(map(lowercase, names))
print(nameList)
print('\n')