import asyncio

async def hello():
    await asyncio.sleep(3)
    print('Hello!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(hello())
    loop.close()