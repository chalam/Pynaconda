import asyncio


# Decorator to mark generator-based coroutines
@asyncio.coroutine
def hello():
    yield from asyncio.sleep(3)
    print('Hello!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # blocking call
    loop.run_until_complete(hello())