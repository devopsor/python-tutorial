#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# Hello world! (<_MainThread(MainThread, started 13820)>)
# Hello world! (<_MainThread(MainThread, started 13820)>)
# Hello again! (<_MainThread(MainThread, started 13820)>)
# Hello again! (<_MainThread(MainThread, started 13820)>)