##########################################multitask###########################################
# Many students have heard that modern operating systems such as Mac OS X, UNIX, Linux, Windows, etc., 
# are operating systems that support "multitasking".

# What is "multitasking"? 
# Simply put, the operating system can run multiple tasks at the same time. 
# For example, you are using a browser to surf the Internet, listening to MP3, and using Word to catch up on homework. 
# This is multitasking, and at least 3 tasks are running at the same time. There are also many tasks quietly running 
# in the background at the same time, just not displayed on the desktop.

# Now, multi-core CPUs are very common, but even single-core CPUs of the past can perform multitasking. 
# Since the CPU execution code is executed sequentially, how does a single-core CPU perform multitasking?
# The answer is that the operating system alternately executes each task, task 1 executes for 0.01 seconds, 
# switches to task 2, task 2 executes for 0.01 seconds, then switches to task 3, executes for 0.01 seconds... 
# and so on. On the surface, each task is executed alternately, but because the CPU is so fast, we feel as if all tasks are 
# executing at the same time.

# Real parallel multitasking can only be implemented on multi-core CPUs. 
# However, since the number of tasks is much more than the number of CPU cores, 
# the operating system will automatically schedule many tasks to be executed on each core in turn.

# For the operating system, a task is a process. For example, opening a browser will start a browser process, 
# opening a notepad will start a notepad process, and opening two notepads will start two notes. 
# In this process, opening a Word starts a Word process.

# Some processes also do more than one thing at the same time, such as Word, which can do typing, spell checking, 
# printing, etc. at the same time. In a process, if you want to do multiple things at the same time, you need to run multiple 
# "subtasks" at the same time. We call these "subtasks" in the process as threads.

# Since each process has to do at least one thing, a process has at least one thread. Of course, a complex process like 
# Word can have multiple threads, and multiple threads can execute at the same time. The execution method of multiple 
# threads is the same as that of multiple processes. The threads all alternate briefly and appear to be executing at the same 
# time. Of course, true simultaneous multi-threading requires multi-core CPUs to be possible.

# All the Python programs we wrote earlier are processes that execute a single task, that is, there is only one thread. 
# What if we want to perform multiple tasks at the same time?

# There are two solutions:
# One is to start multiple processes. 
# Although each process has only one thread, multiple processes can perform multiple tasks together.

# Another method is to start a process and start multiple threads within a process, so that multiple threads can also 
# perform multiple tasks together.

# Of course, there is a third method, which is to start multiple processes, and each process starts multiple threads, 
# so that more tasks are performed at the same time. Of course, this model is more complicated and is rarely used in practice.
# To sum up, there are three ways to implement multitasking:

# multi-process mode;
# multithreaded mode;
# Multi-process + multi-thread mode.

# Execute multiple tasks at the same time. Usually, each task is not unrelated, but needs to communicate and coordinate 
# with each other. Sometimes, task 1 must be suspended and wait for task 2 to complete before continuing to execute. 
# Sometimes, task 3 and task 4 cannot be executed at the same time. , so the complexity of multi-process and multi-threaded 
# programs is much higher than the single-process and single-threaded programs we wrote earlier.

# Because the complexity is high and debugging is difficult, we don't want to write multitasking if we don't have to. 
# However, there are many times when it just doesn't work without multitasking. If you think about watching movies 
# on the computer, one thread must play the video and another thread plays the audio. Otherwise, if a single thread is 
# implemented, you can only play the video first and then play the audio, or play the audio first and then play the video. 
# This obviously doesn't work.

# Python supports both multiprocessing and multithreading, and we'll discuss how to write multitasking programs for both.


################################### Summary ######################################################
# A thread is the smallest unit of execution, and a process consists of at least one thread. 
# How to schedule processes and threads is completely determined by the operating system, and the program itself 
# cannot decide when to execute and how long to execute.