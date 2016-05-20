#!usr/bin/python
from socket import *
from threading import Thread
import sys
s = socket(AF_INET, SOCK_STREAM)
host = 'localhost'
port = 9989          

s.connect((host, port))

def recv():
   while True:
       data= s.recv(1024)
       if not data:
           sys.exit(0)
       print data

Thread( target=recv).start()

while True:
    data = raw_input('')
    s.send(data)

s.close()
