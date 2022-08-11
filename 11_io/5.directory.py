########################################Dir########################################
#If we want to operate files and directories, we can enter various commands provided by the operating system 
# under the command line to complete. For example dir, cp and so on

# What if you want to perform operations on these directories and files in a Python program? In fact, the commands 
# provided by the operating system simply call the interface functions provided by the operating system. 
# The built-in osmodules of Python can also directly call the interface functions provided by the operating system.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
    
# $ python 5.directory.py 
#       Size     Last Modified  Name
# ------------------------------------------------------------
#       4274  2022-08-11 16:48  1.introduce.py
#       2464  2022-08-11 17:10  2.readwrite.py
#        879  2022-08-11 17:24  3.stringio.py
#        755  2022-08-11 17:26  4.bytesio.py
#       1093  2022-08-11 17:31  5.directory.py