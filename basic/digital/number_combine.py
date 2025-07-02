import asyncio

async def number_combine_1():
    print("number_combine_1")


async def number_combine_2():
    print("number_combine_2")


if __name__ == '__main__':
    asyncio.run(number_combine_1())
    asyncio.run(number_combine_2())
