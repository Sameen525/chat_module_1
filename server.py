'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8297 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(2)
print 'Socket now listening'
conn={}
addr={}
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn[0].send('Welcome to the server. Type something and hit enter\n') #send only takes string
    conn[1].send('Welcome to the server. Type something and hit enter\n') 
    #infinite loop so that function do not terminate and thread do not end.
    
    while True:
       
       data = conn[1].recv(1024)
       data1 = conn[0].recv(1024)
       if data:
             reply1 = "client1>>" + data
      
             print reply1
             
             conn[0].sendall(reply1)
             
             
       if not data:
           break
       
       if data1:
             reply2 = "client2>>" + data1
             print reply2
           
             conn[1].sendall(reply2)
             

       if not data1:
           break
       

    conn[0].close()
    conn[1].close()   
 
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn[0], addr[0] = s.accept()
    print 'Connected with ' + addr[0][0] + ':' + str(addr[0][1])
    conn[1], addr[1] = s.accept()
    print 'Connected with ' + addr[1][0] + ':' + str(addr[1][1])
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
