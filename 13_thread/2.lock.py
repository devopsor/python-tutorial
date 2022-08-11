########################################Lock########################################

# The biggest difference between multithreading and multiprocessing is that in multiprocessing, 
# a copy of the same variable exists in each process without affecting each other, 
# while in multithreading, all variables are shared by all threads, 
# so any one Variables can be modified by any thread. Therefore, the biggest danger of sharing data 
# between threads is that multiple threads change a variable at the same time, and the content is changed.

import time, threading

# Assuming this is your bank deposit:
balance = 0

def change_it(n):
    # Store before fetch, the result should be 0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) #8
print('\n')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

# Assuming this is your bank deposit:
balance = 0
lock = threading.Lock()

def change_it(n):
    # Store before fetch, the result should be 0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # To acquire the lock first:
        lock.acquire()
        try:
            # Feel free to change it:
            change_it(n)
        finally:
            # Be sure to release the lock after changing:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  #0

# The advantage of locks is to ensure that a certain key code can only be completely executed by one thread 
# from beginning to end. Of course, there are many disadvantages. 
# The first is to prevent the concurrent execution of multiple threads. 
# A certain code containing locks can only be executed in single-threaded mode. 
# Execution, the efficiency is greatly reduced. 
# Secondly, since there can be multiple locks, when different threads hold different locks and try to 
# acquire the locks held by the other party, it may cause a deadlock, causing multiple threads to hang up, 
# neither executing nor ending. Can only be forced to terminate by the operating system.
