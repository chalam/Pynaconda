import socket

s = socket.socket()
host = socket.gethostname() # get machine name
port = 12345        # reserve a port
s.bind((host, port))  # bind to port

s.listen(5)         # wait for client conn
print('Server listening on port: %d' % port)
while(True):
    c, addr = s.accept()    # estd conn with client
    print('Got connection from', addr)
    c.send(b'Hello from Server')
    c.close()       # close the conn