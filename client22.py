import socket               # Import socket module
import sys
from thread import *
 

Sock = socket.socket()         
host = socket.gethostname()
port = 8989               # Reserve a port for your service.
 
Sock.connect((host, port))

def recv():
    while True:  
        #Receiving from client        
	data = Sock.recv(1024)
        print data

name = raw_input("Enter Your Name : ")
Sock.send(name)

start_new_thread(recv,())
while 1:		
	    reply= raw_input()
            Sock.send(reply)
	   
	    if reply == 'exit' :
	     break

Sock.close()	
