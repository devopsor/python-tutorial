#####################################Coroutine####################################
# Before learning the asynchronous IO model, let's first understand coroutines.
# Coroutines, also known as microthreads, fibers. English name Coroutine.

# The concept of coroutines has been around for a long time, but it was only in the last few years that it became 
# widely used in some languages ​​(such as Lua).

# Subroutines, or functions, are called hierarchically in all languages. 
# For example, A calls B, B calls C during execution, C returns after execution, B returns after execution, 
# and finally A completes execution.

# Therefore, the subroutine call is implemented through the stack, and a thread executes a subroutine.
# Subroutine calls are always one entry, one return, and the calling sequence is unambiguous. 
# Coroutine calls are different from subroutines.

# A coroutine looks like a subroutine, but during execution, it can be interrupted inside the subroutine, 
# and then turn to execute other subroutines, and then return to continue execution at an appropriate time.

# Note that interrupting in a subroutine to execute other subroutines is not a function call, which is somewhat 
# similar to CPU interrupts. For example, subroutines A and B:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# [PRODUCER] Producing 1...
# [CONSUMER] Consuming 1...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 2...
# [CONSUMER] Consuming 2...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 3...
# [CONSUMER] Consuming 3...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 4...
# [CONSUMER] Consuming 4...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 5...
# [CONSUMER] Consuming 5...
# [PRODUCER] Consumer return: 200 OK


# Notice that the consumer function is one generator, after consumer passing one produce in:

# 1. First call c.send(None) the startup generator;
# 2. Then, once something is produced, by c.send(n) switching to consumer execute;
# 3. consumer by yield getting the message, processing it, and passing yield the result back;
# 4. produce get consumerthe result of the processing and continue to produce the next message;
# 5. produce decided not to produce, by c.close() closing consumer, the whole process ended.
# 6. The entire process is lock-free, executed by one thread, produceand consumer cooperates to complete tasks, 
#      so it is called "coroutine" rather than preemptive multitasking of threads.

#Finally, apply a sentence from Donald Knuth to summarize the characteristics of coroutines:

# "Subroutines are a special case of coroutines."

