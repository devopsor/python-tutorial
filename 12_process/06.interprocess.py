# ##############################interprocess communication############################
# ProcessThere is definitely a need for communication between them, and the operating system provides 
# many mechanisms to achieve inter-process communication. 
# Python's multiprocessing modules wrap the underlying mechanism and provide Queue various Pipes ways to 
# exchange data.

# Let's take Queueas an example, create two child processes in the parent process, one Queueto write data 
# and one Queueto read data from it:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

# The code executed by the write data process:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# The code executed by the read data process:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # The parent process creates a Queue and passes it to each child process:
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # Start the child process pw, write:
    pw.start()
    # Start the child process pr, read:
    pr.start()
    # Wait for pw to end:
    pw.join()
    # There is an infinite loop in the pr process, you cannot wait for it to end, you can only forcibly terminate:
    pr.terminate()
    

# The results are as follows:

# Process to write: 1588
# Put A to queue...    
# Process to read: 8916
# Get A from queue.    
# Put B to queue...
# Get B from queue.
# Put C to queue...
# Get C from queue.
# Put D to queue...
# Get D from queue.

# Under Unix/Linux, multiprocessing modules encapsulate fork() calls so that we don't need to pay attention 
# fork() to the details. Since Windows is not fork called, the effect multiprocessing needs to be "simulated" fork. 
# All Python objects of the parent process must be serialized by pickle and then passed to the child process. 
# Therefore, if multiprocessing the call fails under Windows, first consider whether the pickle fails. .

############################# Summary ############################# 
# Under Unix/Linux, fork()multiple processes can be implemented using calls.
# To implement cross-platform multiprocessing, you can use multiprocessing modules.
# Interprocess communication is achieved through Queue, Pipes etc.