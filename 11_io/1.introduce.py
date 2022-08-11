########################################IO###########################################
# IO refers to Input/Output in the computer, that is, input and output. 
# Since programs and runtime data reside in memory and are executed by the ultra-fast computing core of the CPU, 
# where data exchange is involved, usually disks, networks, etc., IO interfaces are required.

# For example, if you open a browser and visit the Yahoo homepage, 
# the browser program needs to obtain Yahoo's webpage through network IO. The browser will first send data to 
# the Yahoo server, telling it that I want the HTML # of the home page. This action is to send data out, called Output, 
# and then the Yahoo server sends the web page. This action is to receive data from the outside, called Input. 
# Therefore, usually, when the program completes the IO operation, there will be two data streams of Input and Output. 
# Of course, there are cases where only one is used. 
# For example, when reading a file from disk to memory, there is only an Input operation. 
# Conversely, writing data to a disk file is only an Output operation.

# In IO programming, Stream is a very important concept. 
# You can think of a stream as a water pipe, and data is the water in the water pipe, but it can only flow in one direction. 
# Input Stream is the flow of data into memory from the outside (disk, network), 
# and Output Stream is the flow of data from memory to the outside. 
# For web browsing, at least two water pipes need to be established between the browser and the Yahoo server 
# so that data can be sent and received.

# Since the speed of CPU and memory is much higher than the speed of peripherals, there is a serious mismatch of 
# speed in IO programming. For example, if you want to write 100M of data to the disk, it only takes 0.01 seconds for 
# the CPU to output 100M of data, but it may take 10 seconds for the disk to receive the 100M of data. 
# What should I do? There are two ways:

# The first is that the CPU waits, that is, the program suspends the execution of subsequent codes, waits for 100M of 
# data to be written to the disk after 10 seconds, and then executes it downwards. This mode is called synchronous IO;

# Another method is that the CPU does not wait, but just tells the disk, "You keep writing slowly, don't worry, I will go on 
# to other things", so the subsequent code can be executed immediately, this mode is called asynchronous IO.

# The difference between synchronous and asynchronous is whether to wait for the result of IO execution. 
# For example, when you go to McDonald's to order, you say "let's have a hamburger", the waiter tells you, 
# sorry, the hamburger needs to be made fresh, and it takes 5 minutes, so you stand in front of the cashier and 
# wait for 5 minutes, get the hamburger, and then go to the mall , which is synchronous IO.

# You say "let's have a hamburger", the waiter tells you that the hamburger needs to wait 5 minutes, you can go to 
# the mall first, and we will notify you when it is ready, so that you can go to do other things (go to the mall) immediately, 
# this is is asynchronous IO.

# Obviously, the performance of using asynchronous IO to write programs will be much higher than that of 
# synchronous IO, but the disadvantage of asynchronous IO is that the programming model is complex. 
# Come to think of it, you have to know when to notify you that "the burger is ready," 
# and there are different ways to notify you. 
# If a waiter comes over to find you, this is callback mode, 
# and if the waiter texts you to notify you, you have to keep checking your phone, which is polling mode. 
# In short, the complexity of asynchronous IO is much higher than that of synchronous IO.

# The ability to operate IO is provided by the operating system. Every programming language encapsulates 
# the low-level C interface provided by the operating system for ease of use, and Python is no exception. 
# We will discuss Python's IO programming interface in detail later.
# Note that the IO programming is all in synchronous mode. Due to the high complexity of asynchronous IO, 
# we will discuss it later when it comes to server-side program development.
