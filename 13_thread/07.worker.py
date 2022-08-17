########################################Worker###################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# Create a similar QueueManager:
class QueueManager(BaseManager):
    pass

# Since this QueueManager only gets the Queue from the network, only the name is provided when registering:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# Connect to the server, which is the machine running task_master.py:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# Note that the port and verification code should be exactly the same as those set in task_master.py:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# Connecting from the Internet:
m.connect()
# Get the object of Queue:
task = m.get_task_queue()
result = m.get_result_queue()
# Get the task from the task queue and write the result to the result queue:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# End of processing:
print('worker exit.')