# Higher-order functions are called Higher-order functions in English. What is a higher-order function? 
# Passing a function as a parameter is called a higher-order function (※)
# and functional programming refers to this highly abstract programming paradigm.

# Variables can point to functions

# Take Python's built-in function for finding absolute values abs()​ ​as an example, 
# use the following code to call this function:
print(abs(-10)) #10

# But what if it's just writing abs
print(abs) #<built-in function abs>
# It can be seen that it abs(-10) is the function call, abs is function itself.

# To get the result of a function call, we can assign the result to a variable:
x = abs(-10)
print(x) #10

# But what if you assign the function itself to a variable?
x = abs
print(x) #<built-in function abs>

# Conclusion: 
# The function itself can also be assigned to the variable, that is: the variable can point to the function.

# If a variable points to a function, can the function be called through the variable? Verify it with code:
f = abs
print(f(-10)) #10

# success! The description variable fnow points to the absfunction itself. 
# Calling a abs() function directly is f() exactly the same as calling a variable.

# The function name is also a variable
# So what is the function name? The function name is actually a variable that points to the function! 
# For abs()this function, the function name can be absregarded as a variable, 
# which points to a function that can calculate the absolute value!

# What happens if you abspoint to other objects?
# abs = 10             # abs function in python lib is overwritten by 10
# print(abs) #10

abs1 = 10
print(abs1) #10

# print(abs(-10)) #TypeError: 'int' object is not callable
import builtins #This module provides direct access to all ‘built-in’ identifiers of Python
x = builtins.abs(-10)
print(x) #10

x = abs(-10)
print(x) #10

###############################Incoming Function##########################
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs)) #11




