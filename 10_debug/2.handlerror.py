######################################Error Handling#####################################

# In the process of running the program, if an error occurs, an error code can be returned by agreement in advance, 
# so that you will know whether there is an error and the reason caused the error. It is very common to return error 
# codes in calls provided by the os. 
# For example, a function that opens a file open() returns the file descriptor (that is, an integer) when successful, 
# and returns when there is an error -1.

# It is very inconvenient to use the error code to indicate whether there is an error, because the normal result that 
# the function itself should return is mixed with the error code, so the caller must use a lot of code to determine 
# whether there is an error:
# err.py
def foo(s):
    return 10 / int(s)  #ZeroDivisionError: division by zero
def bar(s):
    return foo(s) * 2
def main():
    bar(0)
# main()  #ZeroDivisionError: division by zero

# Once an error occurs, it must be reported level by level until a function can handle the error (for example, 
# output an error message to the user).
# So high-level languages ​​usually have a built-in set try...except...finally...of error handling mechanisms, and Python
# is no exception.

#########################################try############################################
# Let's use an example to see try the mechanism:
def fun(n):
    try:
        print('try...')
        r = 10 / n
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except TypeError as e:
        print('except:',e)
    finally:
        print('finally...')
    print('END')

fun(0)
# try...
# except: division by zero
# finally...
# END
fun(1)
# try...
# result: 10.0
# finally...
# END
fun('a')
# try...
# except: unsupported operand type(s) for /: 'int' and 'str'
# finally...
# END
print('\n')

# In addition, if no error occurs, you can except add one after the statement block else, when no error occurs, 
# the else statement will be executed automatically:
def fun(n):
    try:
        print('try...')
        r = 10 / int(n)
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

fun(1)
# try...
# result: 10.0
# no error!
# finally...
# END
fun('a')
#try...
# ValueError: invalid literal for int() with base 10: 'a'
# finally...
# END
print('\n')

# There is also a huge advantage of using try...except catching errors, that is, you can call across multiple layers, 
# such as function main() calls bar(), bar() calls foo(), and the result is foo() an error. At this time, as long as it 
# main() is caught, it can be processed:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main(n):
    try:
        bar(n)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main('0')
# Error: division by zero
# finally...

main('s')
# Error: invalid literal for int() with base 10: 's'
# finally...

# That is, you don't need to catch errors at every possible place, just at the appropriate level. try...except...finally 
# In this way, the trouble of writing is greatly reduced .
print('\n')

#######################################call stack##########################################

# If the error is not caught, it just keeps going up and is caught by the Python interpreter, prints an error message, 
# and the program exits.
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
# main()   # Traceback (most recent call last):
print('\n')

# The outputs are as follows:
# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 130, in <module>
#     main()
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 128, in main
#     bar('0')
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 125, in bar
#     return foo(s) * 2
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 122, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero

# When an error occurs, be sure to analyze the wrong call stack information in order to locate the wrong location.

####################################### log error ###########################################

# If you don't catch the error, you can have the Python interpreter print the error stack, but the program is terminated. 
# Now that we can catch the error, we can print the error stack, analyze the cause of the error, and let the program 
# continue.
# Python's built-in logging module makes logging error messages very easy:
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    print('END')

main()
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 160, in main
#     bar('0')
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 156, in bar
#     return foo(s) * 2
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 153, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# END
# Through configuration, loggingerrors can also be recorded in the log file, which is convenient for later investigation.
print('\n')

#######################################throw error########################################
# Because errors are classes, catching an error is catching an instance of that class. So errors are not created 
# out of thin air, but are intentionally created and thrown. Python's built-in functions throw many types of errors, 
# and functions we write ourselves can throw errors as well.

# If you want to throw an error, you can first define an error class according to your needs, choose a good inheritance 
# relationship, and then use the raise statement to throw an error instance:
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0')

# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 195, in <module>
#     foo('0')
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 192, in foo     
#     raise FooError('invalid value: %s' % s)
# __main__.FooError: invalid value: 0

# Only define our own error types when necessary. If you can choose one of Python's built-in error types 
# (eg ValueError, TypeError), try to use Python's built-in error types.
print('\n')

# Finally, let's look at another way of error handling:
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()
# The outputs are as follows:
# ValueError!
# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 222, in <module>      
#     bar()
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 217, in bar
#     foo('0')
#   File "C:\workspace\Python\python_tutorials\10_debug\2.handlerror.py", line 212, in foo
#     raise ValueError('invalid value: %s' % s)
# ValueError: invalid value: 0
