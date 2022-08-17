##########################################Filter#####################################
# Python built-in filter() functions are used to filter sequences.

# filter()  accepts a function and a sequence. 
# The difference to map()  is that filter() 
# the incoming function is applied to each element in turn,                              (※)
# and then the element is retained or discarded according to the return True (※)
# For example, in a list, to remove even numbers and keep only odd numbers, you can write:

def isOdd(n):
    return n % 2 == 1
checkOdd = list(filter(isOdd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(checkOdd) #[1, 5, 9, 15]
odd = list(map(isOdd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(checkOdd) #[True, False, False, True, False, True, False, True]
print('\n')
# from functools import reduce
# checkOdd = list(reduce(isOdd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(checkOdd)  #TypeError: isOdd() takes 1 positional argument but 2 were given

def notEmpty(s):
    return s and s.strip()
checkEmpty = list(filter(notEmpty, ['A', '', 'B', None, 'C', '  ']))
print(checkEmpty) #['A', 'B', 'C']

checkEmpty = list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  ']))
print(checkEmpty) #['A', 'B', 'C']

# It can be seen filter() that the key to using this higher-order function is to 
# correctly implement a "filtering" function.

# Note that filter() the function returns a Iterator, which is a lazy sequence, 
# so to force filter() the completion of the calculation results, you need to use the list() function to 
# get all the results and return the list.

# To implement this algorithm in Python, we can start by constructing a 3　sequence of odd numbers 
# starting from:
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# Note that this is a generator and an infinite sequence.
def _not_divisible(n):
    return lambda x: x % n > 0
# Finally, define a generator that keeps returning the next prime number:
def primes():
    yield 2
    it = _odd_iter() # initialize the sequence
    while True:
        n = next(it) # return the first item
        print(n)
        yield n
        it = filter(_not_divisible(n), it) # construct new sequence

# This generator first returns the first prime number 2, and then uses filter() it to continuously generate 
# filtered new sequences.
# Since it primes() is also an infinite sequence, you need to set a condition to exit the loop when calling:
for n in primes():
    if n < 20:
        print(n)
    else:
        break

# 2
# 3
# 3
# 5
# 5
# 7
# 7
# 11
# 11
# 13
# 13
# 17
# 17
# 19
# 19
# 23

