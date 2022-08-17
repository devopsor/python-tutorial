###########################Anonymous #########################

# When we pass in functions, sometimes, we don't need to explicitly define the function, 
# and it is more convenient to pass in the anonymous function directly.

# In Python, there is limited support for anonymous functions. 
# Taking the map() function as an example, when calculating f(x)=power(x) , in addition to 
# defining a f(x) function, you can also directly pass in an anonymous function:
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# It can be seen that the anonymous function lambda x: x * x is actually:
def fn(x):
    return x*x

# The keyword lambda represents an anonymous function,  (※)
# and the one before the colon x represents the function parameter.

# Anonymous functions have a limitation, that is, there can only be one expression, (※)
# no need to write return, the return value is the result of the expression.
fn1 = lambda x: x * x
print(fn1) #<function <lambda> at 0x000002D08F5F7940>
print(fn1(2)) #4
fn2 =lambda x, y: x * y
print(fn2) #<function <lambda> at 0x000002D08F5F79D0>
print(fn2(2,3)) #6
print(fn1 == fn2) #False

# Similarly, anonymous functions can also be returned as return values, for example:
def build(x, y):
    return lambda: x * x + y * y
print(build(3,4)) #<function build.<locals>.<lambda> at 0x000002A39CC57A60>
print(build(3,4)()) #25
print('\n')

def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

