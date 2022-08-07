###########################Function#########################
#function as return value
# In addition to accepting functions as parameters, higher-order functions can also 
# return functions as result values.
# Let's implement a variadic summation. Typically, the summation function is defined like this:
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3))  #6
print('\n')

# But what if you don't need to sum it right away, but later in the code, 
# recompute it as needed? Instead of returning the result of the summation, 
# it is possible to return the function of the summation:
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
print(lazy_sum(1,2,3))  #<function lazy_sum.<locals>.sum at 0x000001E64EC778B0>
print('\n')
# In the above  example,  lazy_sum define a function in the function sum, 
# and the inner function sum can refer lazy_sum to the parameters and local variables of 
# the outer function. When the lazy_sum function is returned sum, the relevant parameters and 
# variables are saved in the returned function, which is called "" 
# The program structure of "Closure" has great power.  (※)

func = lazy_sum(1,2,3)
print(func)  #<function lazy_sum.<locals>.sum at 0x00000252716A7940>
print('\n')

func = lazy_sum(1,2,3)
#The result of the sum is actually calculated when the function is called :
print(func())  #6

# Note again that when we call lazy_sum(), each call returns a new function, 
# even if the same parameters are passed in:
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2) #False

# f1() The call results of and f2() do not affect each other.
print(f1()) #25
print(f2()) #25

