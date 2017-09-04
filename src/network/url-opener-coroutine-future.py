import asyncio
import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

import time


# async
# 1. non-blocking ops on socket
# 2. callback
# 3. event loop to schedule

# coroutines
# 1. Futures
# 2. generators
# 3. Task

URL = 'http://echo.jsontest.com/key/value/one/two/three/four'
URL = 'https://jsonplaceholder.typicode.com/posts'
selector = DefaultSelector()
n_task = 0


async def get_page(host, path, port=80):
    global n_task
    n_task += 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    try:
        s.connect((host, port))
    except BlockingIOError:
        pass

    f = asyncio.Future()
    selector.register(s.fileno(), EVENT_WRITE, data=f)

    await f

    selector.unregister(s.fileno())

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    chunks = []
    while True:
        f = asyncio.Future()
        selector.register(s.fileno(), EVENT_READ, data=f)
        await f
        selector.unregister(s.fileno())

        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            break

    # finished
    body = (b''.join(chunks)).decode()
    print(body, body)
    n_task -= 1


start = time.time()
Task(get_page('www.google.com', '/search?q=test'))
Task(get_page('www.google.com', '/search?q=test'))
Task(get_page('www.google.com', '/search?q=test'))
Task(get_page('www.google.com', '/search?q=test'))


# get_page('echo.jsontest.com', '/key/value/one/two/three/four')
# get_page('jsonplaceholder.typicode.com', '/posts')


# event-loop!
# while True:
# while n_task:
#     events = selector.select()
#     for key, mask in events:
#         fut = key.data
#         fut.resolve()
#
loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print(future.result())
loop.close()

print('Timed %.1f sec' % (time.time() - start))