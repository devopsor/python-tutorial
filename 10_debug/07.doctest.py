######################################DocTest#####################################
# When we write a comment, if we write a comment like this:
# Certainly more explicitly tells the caller of the function what inputs and outputs the function expects.

# And, Python's built-in "doctest" module can directly extract code in comments and execute tests.
# doctest strictly follows the input and output of the Python interactive command line to determine whether the test 
# results are correct. 
# Only when the test is abnormal, it can be used to ... represent a large piece of annoying output in the middle.

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# Let's test the last written Dict class with doctest:
# python 7.doctest.py 

if __name__=='__main__':
    import doctest
    doctest.testmod()

# Theres was no output. This shows that the doctests we wrote are all correct. 
# If there is a problem with the program, such as __getattr__() commenting out the method, 
# and then running it will report an error:

# $ python 7.doctest.py
# **********************************************************************
# File "C:\workspace\Python\python_tutorials\10_debug\7.doctest.py", line 15, in __main__.Dict
# Failed example:
#     d1.x
# Exception raised:
#     Traceback (most recent call last):
#       File "C:\Python\lib\doctest.py", line 1336, in __run
#         exec(compile(example.source, filename, "single",
#       File "<doctest __main__.Dict[2]>", line 1, in <module>
#         d1.x
#     AttributeError: 'Dict' object has no attribute 'x'
# **********************************************************************
# File "C:\workspace\Python\python_tutorials\10_debug\7.doctest.py", line 21, in __main__.Dict
# Failed example:
#     d2.c
# Exception raised:
#     Traceback (most recent call last):
#       File "C:\Python\lib\doctest.py", line 1336, in __run
#         exec(compile(example.source, filename, "single",
#       File "<doctest __main__.Dict[6]>", line 1, in <module>
#         d2.c
#     AttributeError: 'Dict' object has no attribute 'c'
# **********************************************************************
# 1 items had failures:
#    2 of   9 in __main__.Dict
# ***Test Failed*** 2 failures.
