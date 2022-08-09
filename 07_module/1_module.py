#################################Module#################################
# In the development process of computer programs, as more and more program codes are written, 
# the code in a file will become longer and longer, and it will become more and more difficult to maintain.

# In order to write maintainable code, we group many functions into different files, so that each file 
# contains relatively little code. Many programming languages ​​use this way of organizing code. 
# In Python, a .py file is called a module.(※)

# Benefits of using modules
# The biggest benefit is that the maintainability of the code is greatly improved. 
# Second, writing code doesn't have to start from scratch. When a module is written, 
# it can be referenced elsewhere. When we write programs, we often refer to other modules, 
# including Python built-in modules and modules from third parties.

# Using modules also avoids conflicting function names and variable names. 
# Functions and variables with the same name can exist in different modules, so when we write 
# our own modules, we don't have to consider that the names will conflict with other modules. 
# But also pay attention to try not to conflict with built-in function names. (※)
# Click here to see all of Python's built-in functions.

# You might also think, what if different people write modules with the same name? 
# In order to avoid module name conflicts, Python introduces a method of organizing modules by directory, 
# called a package.(※)

# A module is a collection of Python code that can use or be used by other modules.
# When creating your own modules, keep in mind:

# The module name should follow the Python variable naming convention, and do not use special characters;
# The module name should not conflict with the system module name. 

################################Module#############################

# Python itself has a lot of very useful modules built-in, as long as the installation is complete, 
# these modules can be used immediately.
# Let's take the built-in sysmodule as an example and write a hello module:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Print Hello Module '

__author__ = 'James'

import sys

def printHello():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
        
if __name__=='__main__':
    printHello()
# python module.py 'World!'  ⇒ Hello, Tester!
# python module.py ⇒Hello, world!

################################Scope#############################

# In a module, we may define many functions and variables, but some functions and variables 
# we want to be used by others, and some functions and variables we want to use only inside the module. 
# In Python, this is done through _ underbar prefixes. (※)

# Normal function and variable names are public and can be directly referenced, such as: abc, x123, PI etc.;
# Variables like __xxx__ this are special variables that can be directly referenced, but have special purposes. 
# For example, the above __author__,  __name__special variables, the documentation comments defined by 
# modules can also be accessed using special variables __doc__. 
# Our own variables generally do not use such variable names;

# Functions or variables like _xxx and __xxx such are private and should not be directly referenced, 
# such as _abc, __abc etc.;

#The reason why we say that private functions and variables "should not" be directly referenced, 
# rather than "cannot" be directly referenced, is because Python does not have a way to completely 
# restrict access to private functions or variables. A private function or variable should be referenced.
# Private functions or variables shouldn't be referenced by others, so what's the use of them? See example:
def _private_1(name):
    print('Hello, %s' % name)

def _private_2(name):
    print('Hi, %s' % name)

def greeting(name):
    if len(name) > 3:
         _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    greeting('James') #Hello, James
    
    
################################Install Third-party Modules###############################
# In Python, installing third-party modules is done through the package management tool pip.
# If you are using Mac or Linux, you can skip the step of installing pip itself.
# If you are using Windows, please refer to the section on installing Python pip and make sure that and 
# Add python.exe to Path.

# Try running in a command prompt window pip, if Windows prompts that the command is not found, 
# you can re-run the installer to add it pip.

# Note: It is possible to have both Python 3.x and Python 2.x on Mac or Linux, so the corresponding pip 
# command is pip3.

# For example, we want to install a third-party library Python Imaging Library, which is a very 
# powerful tool library for processing images under Python. However, PIL currently only supports Python 2.7 
# and has not been updated for a few years. Therefore, the development of the Pillow project 
# based on PIL is very active and supports the latest Python 3.

# Generally speaking, third-party libraries will be registered on the official Python pypi.python.org website. 
# To install a third-party library, you must first know the name of the library, which can be searched 
# on the official website or pypi. For example, the name of Pillow is Pillow , So, the command to install Pillow is:
# pip install Pillow
# Once you've patiently waited for it to download and install, you're ready to use Pillow.

# Install common modules

# When using Python, we often need to use many third-party libraries, such as Pillow mentioned above, 
# as well as MySQL drivers, web framework Flask, scientific computing Numpy, etc. It is time-consuming and 
# laborious to install one by one with pip, and compatibility needs to be considered. We recommend using 
# Anaconda (※)
# directly , which is a Python-based data processing and scientific computing platform. It has built-in many 
# useful third-party libraries. When we install Anaconda, it is equivalent to automatically installing dozens 
# of third-party modules. , very easy to use.
