######################################debug#####################################
# In the process of running the program, there will always be various errors.
# Some errors are caused by programming problems. For example, an integer should be output and a string should be 
# output. This kind of error is usually called a bug, and the bug must be fixed.

# Some errors are caused by user input, such as asking the user to enter an email address, and the result is an empty 
# string. This kind of error can be handled by checking the user input.

# Another type of error is completely unpredictable during program execution. For example, when writing a file, the disk 
# is full and cannot be written, or when data is fetched from the network, the network is suddenly disconnected. 
# These kinds of errors are also called exceptions, and usually must be handled in the program, otherwise, the program 
# will terminate and exit due to various problems.

# Python has a built-in exception handling mechanism to help us handle errors.
# In addition, we also need to trace the execution of the program to see if the values ​​of the variables are correct, this 
# process is called debugging. Python's pdb allows us to step through code.

# Finally, writing tests is also important. With good tests, it is possible to run over and over again after the program is 
# modified, ensuring that the program output matches the tests we wrote.