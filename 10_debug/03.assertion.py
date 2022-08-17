######################################Assertion#####################################
# assert means that the expression n != 0 should be True, otherwise, according to the logic of the program 
# running, the code behind will definitely go wrong.
# If the assertion fails, the assertstatement itself throws AssertionError:

# For example, the python code is as follows:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\3.assertion.py", line 16, in <module>
#     main()
#   File "C:\workspace\Python\python_tutorials\10_debug\3.assertion.py", line 14, in main    
#     foo('0')
#   File "C:\workspace\Python\python_tutorials\10_debug\3.assertion.py", line 10, in foo     
#     assert n != 0, 'n is zero!'
# AssertionError: n is zero!

