#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. 
# For example, the following snippet of code prints “hello”, waits 1 second, and then prints “world”:
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world!')
asyncio.run(main())
# hello
# world!

# To actually run a coroutine, asyncio provides three main mechanisms:
# The asyncio.run() function to run the top-level entry point “main()” function (see the above example.)
# Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second, and then 
# print “world” after waiting for another 2 seconds:
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# started at 21:11:09
# hello
# world
# finished at 21:11:12

