########################################ThreadLocal###################################


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

# Create a global ThreadLocal object:
local_school = threading.local()  #※

def process_student():
    # Get the student associated with the current thread:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # Bind the student of ThreadLocal:
    print('main thread...')
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# The results are as follows:

# main thread...
# Hello, Alice (in Thread-A)
# main thread...
# Hello, Bob (in Thread-B)  


# A global variable local_school is an ThreadLocal object, each Thread of which can read and write student 
# properties to it, but do not affect each other. You can think of it local_school as a global variable, 
# but each attribute local_school.studentis a local variable of the thread, which can be read and written arbitrarily 
# without interfering with each other, and there is no need to manage the lock problem, ThreadLocal 
# which will be handled internally.

# It can be understood as a global variable local_school, dict which can not only be used local_school.student, 
# but also bind other variables, such as local_school.teacher and so on.

# ThreadLocal 
# The most commonly used place is to bind a database connection, HTTP request, user identity information, etc. 
# for each thread, so that all the called processing functions of a thread can easily access these resources.

############################################ Summary#############################
# Although a ThreadLocal variable is a global variable, 
# each thread can only read and write an independent copy of its own thread without interfering with each other. 
# ThreadLocal Solved the problem that parameters are passed to each other between functions in a thread.
