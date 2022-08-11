# ########################################Process vs Thread################################

# We introduced multiprocessing and multithreading, two of the most common ways to implement multitasking. 
# Now, let's discuss the pros and cons of both approaches.

# First of all, to achieve multi-tasking, we usually design the Master-Worker mode. 
# The Master is responsible for assigning tasks, and the Worker is responsible for executing tasks. 
# Therefore, in a multi-tasking environment, there is usually one Master and multiple Workers. (※)

# If the Master-Worker is implemented with multiple processes(※), the main process is the Master, 
# and the other processes are the Workers.

# If the Master-Worker is implemented with multiple threads(※), the main thread is the Master, 
# and the other threads are the Workers.

# The biggest advantage of multi-process mode is high stability, 
# because a child process crashes, it will not affect the main process and other child processes. 
# (Of course, the main process hangs up  all the processes, but the Master process is only responsible for 
# allocating tasks, and the probability of  hanging up is low.) 
# The famous Apache first adopted the multi-process mode.(※)

# The disadvantage of the multi-process mode is that the cost of creating a process is high. 
# In Unix/Linux systems, it fork is OK to use calls, and the cost of creating processes in Windows is huge. 
# In addition, the number of processes that the operating system can run at the same time is also limited. 
# Under the constraints of memory and CPU, if there are thousands of processes running at the same time, 
# the operating system will even have scheduling problems.

# Multi-threaded mode is usually a little faster than multi-process, but not much faster, 
# and the fatal disadvantage of multi-threaded mode is that any thread hangs may directly cause 
# the entire process to crash, because all threads share the memory of the process. 
# On Windows, if there is a problem with the code executed by a thread, you can often see this prompt: 
# "The program has performed an illegal operation and is about to close." 
# In fact, there is often a problem with a thread, but the operating system will force End the entire process.

# # Under Windows, multi-threading is more efficient than multi-process, so Microsoft's IIS server adopts 
# multi-threading mode by default. Due to the stability problem of multi-threading, 
# the stability of IIS is not as good as that of Apache. In order to alleviate this problem, IIS and Apache now 
# have a mixed mode of multi-process + multi-threading, which really complicates the problem.

# ########################################Thread Switching################################

# Whether it is multi-process or multi-threaded, 
# as long as the number is large, the efficiency will definitely not go up, why?

# Let's take an analogy. 
# Suppose you are unfortunately preparing for the senior high school entrance examination. 
# You need to do homework in 5 subjects of Chinese, mathematics, English, physics, and chemistry every night. 
# Each homework takes 1 hour.
# If you spend 1 hour doing the language homework first, and then spend 1 hour doing the math homework, 
# and then do it all in turn, it will take a total of 5 hours. This method is called a single-task model, 
# or a batch task model.

# Suppose you plan to switch to a multitasking model, you can do Chinese for 1 minute, 
# then switch to math homework, do 1 minute, then switch to English, and so on, as long as the switching 
# speed is fast enough, this method will be executed with a single-core CPU. Multitasking is the same. 
# From the point of view of a kindergartener, you are doing 5 homework at the same time.

# However, switching homework comes at a cost. For example, when switching from Chinese to mathematics, 
# you must first clean up the Chinese books and pens on the desk (this is called saving the scene), 
# then, open the mathematics textbook and find a compass ruler (this is called preparing for a new environment) ) 
# to start doing math homework. The same is true when the operating system switches processes or threads. 
# It needs to save the currently executed on-site environment (CPU register state, memory page, etc.), 
# and then prepare the execution environment of the new task (restore the last register state, switch memory 
# pages, etc.) to start execution. Although this switching process is fast, it also takes time. 
# If there are thousands of tasks running at the same time, the operating system may be mainly busy switching 
# tasks, and there is not much time to perform tasks.

# Therefore, once the multitasking reaches a limit, it will consume all the resources of the system, resulting in 
# a sharp drop in efficiency, and all tasks cannot be done well.


# ##################################Compute-intensive vs. IO-intensive#######################

# A second consideration for multitasking is the type of task. 
# We can divide tasks into compute-intensive and IO-intensive.

# Computation-intensive tasks are characterized by a large amount of computation and CPU resource consumption, 
# such as calculating the pi ratio, decoding video in high-definition, etc., all of which depend on the computing 
# power of the CPU. Although this kind of computing-intensive task can also be completed by multitasking, 
# the more tasks, the more time spent in task switching, and the lower the efficiency of the CPU to perform tasks. 
# The number of simultaneous tasks should be equal to the number of CPU cores.

# Computation-intensive tasks mainly consume CPU resources, so the efficiency of the code is very important. 
# Scripting languages ​​like Python are inefficient and completely unsuitable for computationally intensive tasks. 
# For computationally intensive tasks, it is best to write in C.

# The second type of task is IO-intensive. Tasks involving network and disk IO are all IO-intensive tasks. 
# This type of task is characterized by low CPU consumption and most of the time of the task is waiting for the 
# IO operation to complete (because The speed of IO is much lower than the speed of CPU and memory). 
# For IO-intensive tasks, the more tasks, the higher the CPU efficiency, but there is a limit. Most common tasks 
# are IO-intensive tasks, such as web applications.

# During the execution of IO-intensive tasks, 99% of the time is spent on IO, and very little time is spent 
# on the CPU. Therefore, it is completely impossible to replace the extremely slow scripting language such as 
# Python with the extremely fast C language. Improve operational efficiency. For IO-intensive tasks, the most 
# suitable language is the language with the highest development efficiency (the least amount of code), 
# the scripting language is the first choice, and the C language is the worst.


# ##################################Asynchronous IO#######################
# Considering the huge speed difference between CPU and IO, a task spends most of the time waiting for IO 
# operations during execution. 
# The single-process single-threaded model will prevent other tasks from being executed in parallel. 
# Therefore, we need a multi-process model. Or a multithreading model to support concurrent execution of 
# multiple tasks.

# Modern operating systems have made huge improvements to IO operations, and the biggest feature is 
# support for asynchronous IO. 
# If you make full use of the asynchronous IO support provided by the operating system, you can use 
# a single-process single-thread model to perform multitasking. This new model is called an event-driven model. 
# Nginx is a web server that supports asynchronous IO. It runs on a single-core CPU. The single-process model 
# can efficiently support multitasking. On a multi-core CPU, you can run multiple processes (the same number 
# as the number of CPU cores), taking full advantage of the multi-core CPU. Because the total number of processes 
# in the system is very limited, the operating system scheduling is very efficient. Multitasking with the asynchronous 
# IO programming model is a major trend.
# Corresponding to the Python language, the single-threaded asynchronous programming model is called coroutines. 
# With the support of coroutines, efficient multitasking programs can be written based on event driving. 
# We'll discuss how to write coroutines later.