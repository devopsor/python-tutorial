########################################Fork########################################
# To make a Python program implement multiprocessing, we must first understand the relevant knowledge of 
# the operating system.

# Unix/Linux operating systems provide a fork() system call which is very special. 
# Ordinary function calls, 
# call once, return once, 
# but fork() call once, return twice, 
# because the operating system 
# automatically copies the current process (called the parent process) (called the child process), and then, 
# respectively, in the parent process and the child process. In-process return.

# The child process returns forever 0, while the parent process returns the ID of the child process. getppid() 
# The reason for this is that a parent process can fork many child processes, so the parent process needs to 
# record the ID of each child process, and the child process can get the ID of the parent process only by calling .

# Python os modules encapsulate common system calls, including fork the ability to easily create subprocesses 
# in a Python program:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# The results are as follows:
# Process (985) start...
# I (985) just created a child process (986).
# I am child process (986) and my parent is 985.

# fork The code above won't work on Windows 
# since Windows doesn't call it. 
# The Mac system is based on the BSD (a type of Unix) kernel, so it is no problem to run under the Mac. 
# It is recommended that you use the Mac to learn Python!

# With the fork call, a process can copy a child process to handle the new task when it receives a new task. 
# The common Apache server is that the parent process listens to the port. Whenever there is a new http request, 
# it will fork the child process. Handle new http requests.