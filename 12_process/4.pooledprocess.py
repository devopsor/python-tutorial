########################################Multiprocessing########################################

# If you want to start a large number of subprocesses, you can create subprocesses in batches in a process pool:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# The results are as follows:

# Parent process 12240.
# Waiting for all subprocesses done...
# Run task 0 (6056)...
# Run task 1 (1504)... 
# Run task 2 (9324)... 
# Run task 3 (12004)...
# Task 1 runs 0.78 seconds.
# Run task 4 (1504)...
# Task 2 runs 1.28 seconds.
# Task 3 runs 2.14 seconds.
# Task 4 runs 1.82 seconds.
# Task 0 runs 2.70 seconds.
# All subprocesses done.

#################################### Code interpretation #####################################
# Pool Calling a method on an object join() will wait for all child processes to complete execution. 
# join() 
# It must be called before calling close(), and close() new ones cannot be added after the call Process.
# Please pay attention to the output results, task 0, 1, 2, 3 are executed immediately, and task 4 will be executed 
# after the completion of a previous task. This is because Pool the default size is 4 on my computer, 
# so at most 4 processes can be executed at the same time.This is an Pool intentional design limitation, 
# not an operating system limitation. If changed to:
# p = Pool(5)
# You can run 5 processes at the same time.
