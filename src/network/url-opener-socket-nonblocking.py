import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

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
    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    selector.unregister(s.fileno())

    s.send(request.encode())

    chunks = []
    while True:
        selector.register(s.fileno(), EVENT_READ)
        selector.select()
        selector.unregister(s.fileno())

        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body, body)
            return

get_page('www.google.com', '/search?q=test')
# get_page('echo.jsontest.com', '/key/value/one/two/three/four')
# get_page('jsonplaceholder.typicode.com', '/posts')