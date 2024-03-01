import asyncio

async def task1():
    for i in range(10):
        print("task-1: counting", i)
        await asyncio.sleep(1)

async def task2():
    for i in range(10):
        print("task-2: counting", i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(task1(), task2())

if __name__ == '__main__':
    asyncio.run(main())