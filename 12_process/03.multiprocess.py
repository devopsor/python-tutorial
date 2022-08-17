########################################Multiprocessing########################################

# If you plan to write a multi-process service program, Unix/Linux is undoubtedly the right choice. 
# Since Windows does not fork call, is it not possible to write multi-process programs in Python on Windows?

# Since Python is cross-platform, it should naturally provide a cross-platform multi-process support. 
# multiprocessing A module is a cross-platform version of a multi-process module.

# multiprocessing
# The module provides a Process class to represent a process object, the following example demonstrates 
# starting a child process and waiting for it to finish:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

# The code to be executed by the child process
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# The results are as follows:

# $ python 3.multiprocess.py 
# Parent process 10024.
# Child process will start.
# Run child process test (1532)...
# Child process end.


# When creating a child process, you only need to pass in an execution function and the parameters of the function, 
# create an Process instance, and start() start it with a method, which makes it easier than creating a process fork().

# join() 
# The method can wait for the child process to end before continuing to run, 
# usually used for synchronization between processes.
