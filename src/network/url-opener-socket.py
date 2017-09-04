import socket

URL = 'http://echo.jsontest.com/key/value/one/two/three/four'
URL = 'https://jsonplaceholder.typicode.com/posts'


def get_page(host, path, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    chunks = []
    while True:
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