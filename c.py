#!usr/bin/python
from socket import *

host = 'localhost'  # '127.0.0.1' can also be used
port = 52300

sock = socket()
# Connecting to socket

sock.connect((host, port))  # Connect takes tuple of host and port

# Infinite loop to keep client running.


while True:
    msg = raw_input("type:")

    sock.send(msg)
    print 'waiting'

    reply = sock.recv(1024)

    print 'received', repr(reply)

sock.close()
