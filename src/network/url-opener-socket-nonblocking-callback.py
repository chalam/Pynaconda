import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

import time

selector = DefaultSelector()
URL = 'http://echo.jsontest.com/key/value/one/two/three/four'
URL = 'https://jsonplaceholder.typicode.com/posts'


def get_page(host, path, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    try:
        s.connect((host, port))
    except BlockingIOError:
        pass

    callback = lambda: connected(s, path)
    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    callback()


def connected(s, path):
    selector.unregister(s.fileno())
    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    chunks = []
    callback = lambda: readable(s, chunks)
    selector.register(s.fileno(), EVENT_READ)
    selector.select()
    callback()

def readable(s, chunks):
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)

        # we need to make the socket readable again for the next chunk
        callback = lambda: readable(s, chunks)
        selector.register(s.fileno(), EVENT_READ)
        selector.select()
        callback()
    else:
        body = (b''.join(chunks)).decode()
        print(body, body)
        return

start = time.time()

get_page('www.google.com', '/search?q=test')
get_page('www.google.com', '/search?q=test')
get_page('www.google.com', '/search?q=test')
get_page('www.google.com', '/search?q=test')

# get_page('echo.jsontest.com', '/key/value/one/two/three/four')
# get_page('jsonplaceholder.typicode.com', '/posts')

print('Timed %.1f sec' % (time.time() - start))