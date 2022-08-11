########################################Child Process########################################

# Many times, the child process is not itself, but an external process. After we have created the child process, 
# we also need to control the input and output of the child process.
# subprocess Modules allow us to easily start a subprocess and then control its input and output.

# The following example demonstrates how to run a command in Python code nslookup www.python.org, 
# which has the same effect as running it directly from the command line:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('\n')
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
print('\n')

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# The above code is equivalent to executing the command on the command line nslookupand then manually
# entering:
# set q=mx
# python.org
# exit

# The results are as follows:

# $ nslookup www.python.org
# Server:  UnKnown
# Address:  fe80::fab7:97ff:fe5f:9315

# Non-authoritative answer:
# Name:    dualstack.python.map.fastly.net
# Addresses:  2a04:4e42:1a::223
#           151.101.108.223    
# Aliases:  www.python.org     

# Exit code: 0


# $ nslookup
# Default Server:  UnKnown
# Address:  fe80::fab7:97ff:fe5f:9315

# > > Server:  UnKnown
# Address:  fe80::fab7:97ff:fe5f:9315

# python.org      MX preference = 50, mail exchanger = mail.python.org
# >
# Exit code: 0