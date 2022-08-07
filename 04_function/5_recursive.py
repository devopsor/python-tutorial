##################################Recursive Function##############################
#Inside a function, other functions can be called. A function is recursive if it internally calls itself.
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5)) #120

# The above is a recursive function. You can try:
print(fact(1)) #1

#The advantage of recursive functions is that the definition is simple and the logic is clear. 
# In theory, all recursive functions can be written as loops, but the logic of loops is not as clear as recursion.
# When using recursive functions, we  should take care of preventing stack overflow. 
# In the computer, function calls are implemented through the data structure of the stack. 
# Whenever a function call is entered, a stack frame will be added to the stack, and whenever the function returns, 
# the stack will be decremented by one layer. Since the size of the stack is not infinite, 
# too many recursive calls will cause stack overflow. You can try fact(1000):
print(fact(998)) #OK
# print(fact(999)) #RecursionError: maximum recursion depth exceeded in comparison

# When tail-recursive calls are made, the stack will not grow if optimized, 
# so no matter how many calls are made, the stack will not overflow.

# Unfortunately, most programming languages ​​are not optimized for tail recursion, 
# and neither is the Python interpreter, so even changing the above fact(n)function to 
# tail recursion will result in a stack overflow.
print(999*fact(998)) #OK
