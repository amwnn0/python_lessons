import asyncio
import time

async def func1(x):
    print(x)
    await asyncio.sleep(1)
    print('func1')

async def func2(x):
    print(x)
    await asyncio.sleep(1)
    print('func2')

async def main():
    task1 = asyncio.create_task(func1(1))
    task2 = asyncio.create_task(func2(2))

    print(type(task1))

    await task1
    await task2

print(type(func1))
print(type(func1(1)))

print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))

