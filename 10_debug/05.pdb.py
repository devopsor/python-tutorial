######################################PDB#####################################
# The fourth way is to start the Python debugger pdb, let the program run in a single-step mode, 
# and you can view the running status at any time. Let's prepare the program first:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb

s = '0'
n = int(s)
pdb.set_trace() # Running here will automatically pause
print(10 / n)

# After starting with parameters -m pdb, pdb locates the code to be executed next -> s = '0'. 
# Enter the command l to see the code:

# $ python -m pdb 5.pdb.py 
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(8)<module>()
# -> import pdb
# (Pdb) l
#   3     # and you can view the running status at any time. Let's prepare the program first:
#   4
#   5     #!/usr/bin/env python3
#   6     # -*- coding: utf-8 -*-
#   7
#   8  -> import pdb
#   9
#  10     s = '0'
#  11     n = int(s)
#  12     pdb.set_trace() # Running here will automatically pause
#  13     print(10 / n)
# (Pdb) n
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(10)<module>()
# -> s = '0'
# (Pdb) l 
#   5     #!/usr/bin/env python3
#   6     # -*- coding: utf-8 -*-
#   7
#   8     import pdb
#   9
#  10  -> s = '0'
#  11     n = int(s)
#  12     pdb.set_trace() # Running here will automatically pause
#  13     print(10 / n)
# [EOF]
# (Pdb) n
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(11)<module>()
# -> n = int(s)
# (Pdb) l 
#   6     # -*- coding: utf-8 -*-
#   7
#   8     import pdb
#   9
#  10     s = '0'
#  11  -> n = int(s)
#  12     pdb.set_trace() # Running here will automatically pause
#  13     print(10 / n)
# [EOF]
# (Pdb) n
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(12)<module>()
# -> pdb.set_trace() # Running here will automatically pause
# (Pdb) l 
#   7     
#   8     import pdb
#   9
#  10     s = '0'
#  11     n = int(s)
#  12  -> pdb.set_trace() # Running here will automatically pause
#  13     print(10 / n)
# [EOF]
# (Pdb) n
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(13)<module>()
# -> print(10 / n)
# (Pdb) l 
#   8     import pdb
#   9
#  10     s = '0'
#  11     n = int(s)
#  12     pdb.set_trace() # Running here will automatically pause
#  13  -> print(10 / n)
#  14
#  15     # After starting with parameters -m pdb, pdb locates the code to be executed next -> s = '0'.
#  16     # Enter the command l to see the code:
# [EOF]
# (Pdb) n 
# ZeroDivisionError: division by zero
# > c:\workspace\python\python_tutorials\10_debug\5.pdb.py(13)<module>()
# -> print(10 / n)
# (Pdb) p s
# '0'
# (Pdb) p n
# 0
# (Pdb)
# (Pdb) exit()

#Summary

# The most painful thing about writing a program is debugging. The program often runs in an unexpected process. 
# The statement you expect to be executed is actually not executed at all. At this time, debugging is required.
# Although it is more convenient to debug with an IDE, in the end you will find that logging is the ultimate weapon.