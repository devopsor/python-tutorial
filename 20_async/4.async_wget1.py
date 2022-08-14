#################################Async IO#################################
# The syntax async def introduces either a native coroutine or an asynchronous generator. 
# The expressions async with and async for are also valid, and you’ll see them later on
# The keyword await passes function control back to the event loop. 
# (It suspends the execution of the surrounding coroutine.)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.google.com', 'www.google.jp', 'www.yahoo.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()