'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9989 # Arbitrary non-privileged port
ad=[]
i=0  
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


#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
    
    while True:
       
       data = conn.recv(1024)
       
       print data
       if conn== ad[0]:
          
          ad[1].sendall("client1>>"+data)
       else:
          ad[0].sendall("client2>>"+data)
             
       if not data:
             break
    conn.close()   
     

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr= s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    ad.append(conn)
    start_new_thread(clientthread ,(conn,))
    i+=1
s.close()
