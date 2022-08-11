########################################Multi-core CPU###################################

# If you're unlucky enough to have a multi-core CPU, you're definitely thinking that multiple cores should be 
# able to execute multiple threads simultaneously.

# If you write an infinite loop, what will happen?
# Open Mac OS X's Activity Monitor, or Windows' Task Manager, you can monitor the CPU usage of a process.

# We can monitor that an infinite loop thread will occupy 100% of a CPU.
# If there are two infinite loop threads, in a multi-core CPU, it can be monitored that it will occupy 200% of 
# the CPU, that is, occupy two CPU cores.

# In order to run all the cores of the N-core CPU, N infinite loop threads must be started.
# Try writing an infinite loop in Python:
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 10

print(multiprocessing.cpu_count())
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()


# The Python Global Interpreter Lock or GIL, 
# in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

# Starting N threads with the same number of CPU cores, on a 4-core CPU, it can be monitored that 
# the CPU usage is only 102%, that is, only one core is used.

# But using C, C++ or Java to rewrite the same infinite loop, you can directly run all cores, 4 cores run to 400%, 
# 8 cores run to 800%, why not Python?

# Because Python threads are real threads, when the interpreter executes code, there is a GIL lock: 
# Global Interpreter Lock. Before any Python thread is executed, the GIL lock must be obtained first. 
# Then, every 100 bytes of code is executed, the interpreter will The GIL lock is automatically released, 
# giving other threads a chance to execute. This GIL global lock actually locks the execution code of all threads. 
# Therefore, multithreading can only be executed alternately in Python. 
# Even if 100 threads run on a 100-core CPU, only 1 core can be used.

# GIL is a historical legacy of the design of the Python interpreter. 
# Usually, the interpreter we use is the official implementation of CPython. To really take advantage of multi-core, 
# unless you rewrite an interpreter without GIL.
# So, in Python, you can use multithreading, but don't expect to make efficient use of multiple cores. 
# If you must use multiple cores through multithreading, it can only be achieved through C extensions, 
# but this will lose the simplicity and ease of use of Python.

# However, don't worry too much. Although Python cannot use multi-threading to achieve multi-core tasks, 
# it can achieve multi-core tasks through multi-process. Multiple Python processes have their own GIL locks, 
# which do not affect each other.

######################################### Summary ##################################
# Multi-threaded programming has a complex model and is prone to conflicts. It must be isolated by locks. 
# At the same time, be careful of deadlocks.
# Due to the GIL global lock in the design of the Python interpreter, multi-threading cannot take advantage of 
# multi-core. Multithreaded concurrency is a beautiful dream in Python.
