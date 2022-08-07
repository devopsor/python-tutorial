###########################Partial function#########################

#Python functools modules provide many useful functions, one of which is the partial function. 
# It should be noted that the partial function here is not the same as the partial function in the mathematical sense.

# When introducing the function parameters, we mentioned that by setting the default value of the parameter, 
# the difficulty of the function call can be reduced. And partial functions can do this too. An example is as follows:
# int()
# The function can convert strings to integers. (※)
# When only strings are passed in, the int() function converts to 
# decimal by default:
print(int('12345')) #12345


# But the int() function also provides additional base parameters, the default is 10. 
# If you pass basein parameters, you can do N-ary conversion:
print(int('12345', base=8)) #5349
print(int('12345', base=10)) #12345
# print(int('12345', 100)) #ValueError: int() base must be >= 2 and <= 36, or 0
print(int('12345', 32)) #1117317

# Suppose we want to convert a large number of binary strings, it is very troublesome to 
# pass in each time int(x, base=2), so we thought that we can define a int2() function and pass it in 
# by default base=2:
def int2(x, base=2):
    return int(x, base)

# In this way, it is very convenient for us to convert binary:
print(int2('10')) #2
print(int2('1010101')) #85

# functools.partial
# Just to help us create a partial function, we don't need to define it ourselves int2(), we can directly use 
# the following code to create a new function int2:
import functools
int2 = functools.partial(int, base=2)
print(int2('10')) #2
print(int2('1010101')) #85

# Therefore, the function of a simple summary functools.partialis to fix some parameters of a function 
# (that is, set default values), return a new function, and call this new function will be simpler.

# Note that the new int2 function above just base resets the parameter to the default value 2, 
# but other values ​​can also be passed in when the function is called:
print(int2('1000000', base=10)) #1000000

# Finally, when creating a partial function, you can actually receive the function object, *args and **kw 
# these three parameters, when passed in:
int2 = functools.partial(int, base=2)
# Actually fixed the keyword arguments of the int() function base, that is:
int2('10010')
print(int2('10010')) #18
# is equivalent to:
kw = { 'base': 2 }
int('10010', **kw)
print(int('10010', **kw)) #18

# When passing in:
max2 = functools.partial(max, 10)
# In fact, part of as will 10 be *args automatically added to the left, that is:
print(max2(5,6,7,19)) #19

#is equivalent to:
args = (10, 5, 6, 7, 19)
max(*args)
print(max(*args)) #19