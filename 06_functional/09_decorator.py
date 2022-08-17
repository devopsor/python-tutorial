###########################Decorator#########################

#Since a function is also an object, and the function object can be assigned to a variable, 
# the function can also be called through a variable.
def now():
    print('20220819')
f = now
f() #20200819

#The function object has a __name__property that can get the name of the function:
print(now.__name__) #now
print(f.__name__) #now
print('\n')
# Now, suppose we want to enhance now() the function of the function, 
# for example, automatically print the log before and after the function call, 
# but do not want to modify now() the definition of the function, this way of dynamically adding 
# functions during the running of the code is called "decorator" (Decorator ).(※)
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
now = log(now)
# Since log() is a decorator and returns a function, the original now() function still exists, but  the now variable 
# with the same name points to the new function, so the call now() will execute the new function, that is, the log() 
# function returned in the wrapper() function.
now()
# call now():
# 20220819

# wrapper() 
# A function's parameter definition is (*args, **kw), therefore, wrapper() a function that can be called 
# with arbitrary parameters. Inside the wrapper() function, the log is printed first, followed by the call to 
# the original function.
print('\n')

# Observe the above log, since it is a decorator, it takes a function as a parameter, and returns a function.
# We need to use Python's @ syntax to place the decorator at the definition of the function:
@log
def now():
    print('20220819')
# Calling a now()function not only runs now()the function itself, but also now() prints a line of log 
# before running the function:
now()
# call now():
# 20220819
print('\n')

# If the decorator itself needs to pass in parameters, then you need to write a higher-order function that 
# returns the decorator, which will be more complicated to write. For example, to customize the text of the log:
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# The usage of this 3-level nested decorator is as follows:
@log('warning')  #instead of 'call' text
def now():
    print('20220819')
now()
# warning now():
# 20220819  
print('\n')


# Compared with the two-level nested decorator, the effect of 3-level nesting is as follows:
now = log('execute')(now)
now()
# execute wrapper():
# warning now():    
# 20220819
print('\n')

# Let's analyze the above statement, first execute log('execute'), return the decoratorfunction, 
# and then call the returned function, the parameter is the now function, and the return value is finally 
# the wrapper function.

# There is no problem with the definitions of the above two decorators, but there is still one last step. 
# Because we said that functions are also objects, they have __name__equal properties, 
# but if you look at the functions that have been decorated with decorators, they __name__have changed 
# from the original 'now' to 'wrapper':
print(now.__name__) #wrapper
print('\n')
# Because the wrapper() name of the function returned is the same 'wrapper', so you need to __name__ copy 
# the properties of the original function into the wrapper() function, otherwise, some code execution that 
# depends on the function signature will go wrong.
# There is no need to write wrapper.__name__ = func.__name__ such code, Python is built to functools.wraps
# do this, so a complete decorator is written as follows:
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

print(now.__name__) #wrapper
@log  #instead of 'call' text
def now():
    print('20220819')
now()
# wrapper
# call now():
# 20220819
print('\n')

# Or for a decorator with parameters:
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# import functools is the import functools module. The concept of modules will be explained later. 
# For now, just remember wrapper() to prepend the definition @functools.wraps(func)
print(now.__name__) #wrapper
@log('execute')  #instead of 'call' text
def now():
    print('20220819')
now()
# execute now():
# 20220819