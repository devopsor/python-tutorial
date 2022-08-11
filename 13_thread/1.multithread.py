#####################################MultiThreads################################
# Multitasking can be done by multiple processes or by multiple threads within a process.

# We mentioned earlier that a process is composed of several threads, and a process has at least one thread.
# Since threads are execution units directly supported by the operating system, high-level languages ​​usually 
# have built-in support for multithreading, and Python is no exception. 
# Moreover, Python threads are real Posix threads, not simulated threads.

# Python's standard library provides two modules: 

# _thread: are low-level modules,
# threading: high-level modules, which encapsulate pair _thread. 

# In the vast majority of cases, we only need to use threading this advanced module.
# To start a thread is to pass in a function and create an Thread instance, and then call start() to start execution:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

# Code executed by the new thread:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# thread MainThread is running...
# thread LoopThread is running...
# thread LoopThread >>> 1
# thread LoopThread >>> 2
# thread LoopThread >>> 3
# thread LoopThread >>> 4
# thread LoopThread >>> 5
# thread LoopThread ended.
# thread MainThread ended.

# Since any process starts a thread by default, we call this thread the main thread, and the main thread can 
# start a new thread. The Python threading module has a current_thread() function that always returns an instance 
# of the current thread. 
# The name of the main thread instance is called MainThread, and the name of the child thread is specified 
# when it is created. We use the LoopThread name of the child thread. The name is only used for display 
# when printing, and has no other meaning at all. If you don't have a name, Python will automatically name 
# the thread Thread-1,Thread-2 …

