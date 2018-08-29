import socket

s = socket.socket()
host = socket.gethostname() # get machine name
port = 12345        # reserve a port
s.connect((host, port))
print('Received: %s' % s.recv(1024)) # buffered
s.close()       # close the conn