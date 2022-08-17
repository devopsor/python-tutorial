######################################Logging#####################################
# Replace print() with logging is the a way, 
# and better than assert,  logging will not throw an error, and can output to a file:

# For example, the python code is as follows:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# INFO:root:n = 0
# Traceback (most recent call last):
#   File "C:\workspace\Python\python_tutorials\10_debug\4.logging.py", line 16, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

# This is loggingthe advantage, it allows you to specify the level of logging information, there are several levels, 
# debug, 
# info, 
# warning, 
# error etc. 
# When we specify level=INFO, logging.debug does not work. 
# In the same way, after specifying level=WARNING, debug and info will not work. 
# In this way, you can safely output information of different levels without deleting it, 
# and finally control which level of information to output.

# logging
# Another benefit is that with simple configuration, a statement can be output to different places at the same time, 
# such as console and file.
