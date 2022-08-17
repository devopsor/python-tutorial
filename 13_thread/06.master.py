########################################Master###################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# Queue for sending tasks:
task_queue = queue.Queue()
# Queue to receive results:
result_queue = queue.Queue()

# QueueManager inherited from BaseManager:
class QueueManager(BaseManager):
    pass

# Register both Queues on the network, and the callable parameter is associated with the Queue object:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# Bind port 5000, set verification code 'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# Start Queue:
manager.start()
# Get a Queue object accessed over the network:
task = manager.get_task_queue()
result = manager.get_result_queue()
#Put a few tasks in it:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# Read the result from the result queue:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# Close:
manager.shutdown()
print('master exit.')