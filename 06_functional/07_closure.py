###########################Closure#########################

# Note that the returned function references local variables within its definition args, 
# so when a function returns a function, its internal local variables are also referenced 
# by the new function, so closures are simple to use, but not easy to implement.(※)

# Another issue to be aware of is that the returned function does not execute immediately, 
# until it is called f(). Let's look at an example:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print(f1()) #9
print(f2()) #9
print(f3()) #9
print(f1 == f2) #False
print(f1 == f3) #False
# All are 9! The reason is that the returned function references the variable i, 
# but it doesn't execute immediately. By the time all 3 functions return, the variables 
# they refer to ihave become 3, so the final result is 9.
print('\n')

#Note that when returning a closure: the returning function does not refer to any loop variables, (※)
# or variables that will change later.(※)

# What if the loop variable must be referenced? 
# The method is to create another function and use the function's parameters to bind the current value 
# of the loop variable. No matter how the loop variable changes subsequently, 
# the value bound to the function parameter remains unchanged:
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 5):
        print(i)
        fs.append(f(i)) # f(i) is executed immediately, so the current value of i is passed to f()
    return fs
# Look at the result again:
f1, f2, f3, f4 = count()
print(f1()) #1
print(f2()) #4
print(f3()) #9
print(f4()) #16
# The disadvantage is that the code is long, and the code can be shortened by 
# using the lambda function.

###########################Nonlocal#########################

# Using a closure means that the inner function references the local variables of the outer function. (※)
# If we just read the value of the outer variable, we will find that the returned closure function call is fine:
def inc():
    x = 0
    def fn():
        # only read(※)  the value of x:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

# However, if you assign a value to an outer variable, since the Python interpreter will treat it x 
# as fn() a local variable of the function, it will report an error:
def inc():
    x = 0
    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn

# f = inc()
# print(f()) # UnboundLocalError: local variable 'x' referenced before assignment

# The reason is that it is x not initialized as a local variable, and direct calculation x+1 is not possible. 
# But we actually want to refer to inc() the inside of the function x, so we need to fn() add a nonlocal x 
# declaration inside the function. After adding this declaration, the interpreter regards x of fun() 
# as a local variable of the outer function, which has been initialized and can be calculated correctly x+1.

# When using a closure, before assigning a value to an outer variable, you need to 
# use nonlocal to declare that the variable is not a local variable of the current function.
def inc():
    def fn():
        x =0
        x = x + 2
        return x
    return fn

f = inc()
print(f()) # 1
